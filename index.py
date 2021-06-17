from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.in/gp/bestsellers/software/ref=zg_bs_nav_0"

response = requests.get(url)
htmlcontent = response.content

data = BeautifulSoup(htmlcontent)
# print(data.title.string)
# print(data.find_all('a'))
count =1
for img in data.find_all('div'):
    count = count+1
    print(img.get('class'))
print(count)


