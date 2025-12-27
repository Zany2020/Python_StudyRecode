import requests
from requests import head
head = {"User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64)"}
#伪装成浏览器的请求

response = requests.get("http://books.toscrape.com/", headers = head)
print(response)
if response.ok:
    print(response.text)
else:
    print("Failed")