from bs4 import BeautifulSoup
import requests
import pandas as pd

html_data = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks')

soup = BeautifulSoup(html_data.text, 'html.parser')

tables = soup.find_all('table')
table = tables[1]
table_rows = table.find_all('tr')
del table_rows[0]
dc = []

for i in table_rows:
    rows = i.find_all('td')
    for row in rows:
        dcc = []
        txt = row.text.replace('\n','').replace(' ', '')
        dcc.append(txt)
        dc.append(dcc)

names = [i[0].replace('[','') for i in dc[1::3]]
total_assets = [i[0].replace('[','') for i in dc[2::3]]

df = pd.DataFrame(zip(names, total_assets))
df.columns = ['Names', 'Market Cap (US$ Billion)']
print(df.head())
