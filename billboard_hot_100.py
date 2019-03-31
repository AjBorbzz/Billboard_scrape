# Billboard hot 100
import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

data = requests.get('https://www.billboard.com/charts/hot-100')
soup = BeautifulSoup(data.text, 'html.parser')


rank = [i.text.strip() for i in soup.find_all('div', {'class':'chart-list-item__rank'})]
title = [i.text.strip() for i in soup.find_all('div', {'class':'chart-list-item__title'})]
artist = [i.text.strip() for i in soup.find_all('div', {'class':'chart-list-item__artist'})]
data = [rank,title,artist]

extract_date = date.today().strftime("%d%m%Y")
filename = 'billboard_as_at_' + extract_date + '.csv'
with open(filename, 'w') as f:
    csv_writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["Rank","Title","Artist"])
    for x in range(100):
        csv_writer.writerow([data[0][x],data[1][x],data[2][x]])
