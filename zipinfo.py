from bs4 import BeautifulSoup
import os
import sys
import requests
import urllib
import zipfile


url = 'http://fl0c' #Write the site where you will be getting data
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

u=0
for link in soup.find_all('a'):
        u+=1
        if(u>=5):
            file_zip=zipfile.ZipFile("/home/my_project_folder/file/"+link.get('href'),'r')  #directory of the data
            filename=file_zip.namelist()
            data = file_zip.infolist()                
            print(data)
            print (filename)
            print (link)
