import requests
from bs4 import BeautifulSoup
import csv
import webScraper




url = 'https://www.worldometers.info/coronavirus/coronavirus-death-toll/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser") # Parse html

table = soup.find("table", {"class": "table table-hover table-bordered table-condensed table-list"}).find_all("tbody") # table
tr_elems = table[0].find_all("tr") # All rows in table


data = []
first_row = ['Date','Total Deaths','New Deaths','Change in Total Deaths %']
data.append(first_row)
for tr in tr_elems: # Loop through rows
    td_elems = tr.find_all("td") # Each column in row
    data.append([webScraper.convertDigit(td.text.strip()) for td in td_elems])

with open('deathData.csv', 'w', newline='') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(data)

print(data)

