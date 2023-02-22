from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = 'https://expanse.fandom.com/wiki/Category:The_Expanse'
url = 'https://en.wikipedia.org/wiki/The_Expanse_(novel_series)'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table')
print(f"Tables found: {len(tables)}")

choice = int(input('Select table number from 0: '))

data = []
# table = soup.find('table', attrs={'class':'wikitable'})
table = tables[choice]
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

df = pd.DataFrame(data)

print('Data scraped:')
print(df)




