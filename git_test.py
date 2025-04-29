import requests as rq

url = 'https://microview.cz/index.html'

response = rq.get(url=url)
response.raise_for_status()
response_headers = response.headers
for i in response.iter_lines():
    print(i)

print(response_headers)

print(response.text)