from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = 'https://expanse.fandom.com/wiki/Category:The_Expanse'
url = 'https://en.wikipedia.org/wiki/The_Expanse_(novel_series)'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

element = input('Look for html tag: ')

element_list = soup.find_all(element)
print(f"Elements found: {len(element_list)}")

choice = int(input('Select element number from 0: '))

if element == 'table':
    data = []

    table = element_list[choice]
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    df = pd.DataFrame(data)

    print('Data scraped:')
    print(df)
else:
    print(element)



