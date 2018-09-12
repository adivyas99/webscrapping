import urllib
from bs4 import BeautifulSoup
import csv
from datetime import datetime

handle = input("Whose tweets would you like to see? ")
url = "https://twitter.com/"+handle
page = urllib.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

f=soup.title.text
"""
for foo in soup.findAll('a'):
    print(foo.get('href'))
"""
    
m=soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text

i=1
k=[]
for tweet in soup.findAll('div',{"class":'content'}):
	k.append(tweet.find('p').text)



with open('/home/lakshay/Music/filename.csv','a') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow([f,k,m,datetime.now()])
