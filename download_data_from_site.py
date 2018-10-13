#-*- coding='UTF-8' -*-
from bs4 import BeautifulSoup
import os
import sys
import requests
import pymysql
import codecs

conn = pymysql.connect(host='localhost', user='root', password = '!', database ='users', charset ='euckr')

curs = conn.cursor() 

site = requests.get("http://fl0c.info") #Write the place where you will be getting the data

soup = BeautifulSoup(site.text, 'html.parser')
zipfile = soup.find_all("a", href = True)
date = soup.find_all("td")
ipaddress = []
j = 1

for i in zipfile:
   try:
      ipaddress.append((i['href']))
   except:
      pass

for i in range(4, len(ipaddress)):

   index = 2+(i-4)*5
   print(index)
   
   
   os.system('cd /home/ipbank/' + (ipaddress[i])[:-4] + ';cat signCert.cert >> /home/iamkj03/my_project_folder/ipbank/file/'+(ipaddress[i])[:-4])


   date_string = str(date[index])

   index_date = date_string.find('>')

   exact_date = date_string[index_date+1:index_date+11]
   displayed_date = exact_date.split('-')
   print(displayed_date)

   yr = displayed_date[0]
   print(yr)
   mon = displayed_date[1]
   print(mon)
   day = displayed_date[2]
   print(day)
   database_date  = yr + mon + day

   exact_time = date_string[index_date+12:index_date+17]
   displayed_time = exact_time.split(':')
   
   hour = displayed_time[0]
   minute = displayed_time[1]

   database_time = hour + minute

   date_time = database_date + database_time

   print((date_time))




   direc = '/home/ipbank/file/'+(ipaddress[i])[:-4]

   f = codecs.open(direc,'r', encoding='euc-kr', errors = 'ignore')
   person_data = f.read()
   f.close()
   
   ip = (ipaddress[i])[:-4]
   

   print(person_data)
   parse = person_data.split('=')

   parse_name = parse[1].split('()')
   name  = parse_name[0]
   print(name)
   parse_accountNum = parse_name[1].split(',')
   accountNum = parse_accountNum[0]
   print(accountNum)
 
   parse_bank = parse[2].split(',')
   bank = parse_bank[0]
   print(bank)

   country = parse[5] 
   print(country)
 
   sql = "INSERT INTO personal VALUES ( '"+ str(j) +"' , '"+ date_time +"', '"+ name + "' , '"+ bank +"', '"+ accountNum +"' , '"+ ip + "', '"+ country + "')"   

   j += 1

   curs.execute(sql)
   conn.commit()

conn.close()
