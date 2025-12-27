import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
}

response = requests.get(f"https://space.bilibili.com/523995133", headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
all_titles = soup.findAll("a", attrs={"target": "_blank"})
for title in all_titles:
    title_string = (title.string)
    print(title_string)


###失败！！！！！！！！！！！！！！！！！！！
