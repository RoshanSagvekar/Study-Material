import requests
from bs4 import BeautifulSoup
# fetch data using url in byte form
url = "https://www.moneycontrol.com/commodity/"
r = requests.get(url)
print(r.content)
# Convert into html form
soup = BeautifulSoup(r.content, "html")
print(soup.prettify())
# soup.find("tag name", attrs = {html tag attributes})
soup.find('table', attrs={'class':'mctable1'})
# return of findall is all the occurence of the given tag and attributes in list format.
table = soup.findAll('table', attrs={'class':'mctable1'})
table[1]
table_rows = table[1].findAll('tr')
table_rows[0]

for row in table_rows:
  table_data = row.findAll('td')
  print(f"{table_data[0].text} = {table_data[1].text}")