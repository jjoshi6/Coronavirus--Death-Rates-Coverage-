import requests
from bs4 import BeautifulSoup
import csv



def convertDigit(string):
    if string.replace(",", "").isdigit():
        return int(string.replace(",", ""))
    return string

url = 'https://www.worldometers.info/coronavirus/#countries'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser") # Parse html

table = soup.find("table", {"id": "main_table_countries"}).find_all("tbody") # table
tr_elems = table[0].find_all("tr") # All rows in table

data = []
first_row = ['Country, Other','Total Cases','New Cases', 'Total Deaths', 'New Deaths', 'Total Recovered', 'Active Cases', 'Serious Critical', 'Tot Cases/1M Pop']
data.append(first_row)
for tr in tr_elems: # Loop through rows
    td_elems = tr.find_all("td") # Each collumn in row
    data.append([convertDigit(td.text.strip()) for td in td_elems])

print(data)



with open('data.csv', 'w', newline='') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(data)





#rudri was here
