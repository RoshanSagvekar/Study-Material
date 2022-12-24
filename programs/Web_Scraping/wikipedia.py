import requests
from requests.api import request
url="https://en.wikipedia.org/robots.txt"
r=requests.get(url)
data=r.text
print('robots.txt for en.wikipedia.org')
# print('#'*10)
print(data)