from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = 'https://expanse.fandom.com/wiki/Category:The_Expanse'
# url = 'https://en.wikipedia.org/wiki/The_Expanse_(novel_series)'
url = 'https://chorzow.praca.gov.pl/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# tag = input('Look for html tag:` ')
# class_name = input('Look for class name: ')

tag = 'div'
class_name = 'asset-summary'

element_list = soup.find_all(tag, class_= class_name)
print(f"Elements found: {len(element_list)}")

# choice = int(input('Select element number from 0: '))

data = []

def clean(text: str) -> str:
    return text.replace('\n', '').replace('\t', '').strip()

for e in element_list:
    row = []
    day = e.find('span', class_='dayDate').get_text()
    rest = e.find('span', class_='restDate').get_text()
    date = f"{day} {rest.replace('`', ' ')}"
    row.append(date)
    row.append(clean(e.find('h3').get_text()))
    row.append(clean(e.find('p', class_='desktop summary').get_text()))
    data.append(row)



df = pd.DataFrame(data)
df.to_csv('up.txt', index=False, sep='\t')

print('Data scraped:')
print(df)



