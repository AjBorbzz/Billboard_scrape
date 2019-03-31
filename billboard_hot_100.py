# Billboard hot 100
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

data = requests.get('https://www.billboard.com/charts/hot-100')
soup = BeautifulSoup(data.text, 'html.parser')


rank = [i.text.strip() for i in soup.find_all('div', {'class':'chart-list-item__rank'})]
title = [i.text.strip() for i in soup.find_all('div', {'class':'chart-list-item__title'})]
artist = [i.text.strip() for i in soup.find_all('div', {'class':'chart-list-item__artist'})]
data = [rank,title,artist]

with open('billboard.csv', 'w') as f:
    csv_writer = csv.writer(f,delimiter='\t',quoting=csv.QUOTE_MINIMAL) 
    header = ("Rank\t\Title\t\t\t\t\t\tArtist")
    for x in range(100):
        csv_writer.writerow(data[0][x]+"\t"+data[1][x]+"\t\t\t\t\t\t"+data[2][x])
