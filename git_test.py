import requests as rq
import bs4 as bs

url = 'https://microview.cz/index.html'

response = rq.get(url=url)
response.raise_for_status()
response_headers = response.headers
for i in response.iter_lines():
    print(i)

print(response_headers)

print(response.text)

soup = bs.BeautifulSoup(response.text,'html.parser')
print(soup.prettify())

all_p = soup.find_all('p')
for p in all_p:
    print(p)