from bs4 import BeautifulSoup, Tag
import requests

message = 'python'
URL = f'https://www.google.com/search?q={message}'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0, win64; x64) AppleWebKit/537.36 (KHTML., like Gecko) Chrome/68.0.3029.10 Safari/537.3"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
cards = soup.find_all('div', class_ = 'yuRUbf')
data = []
card: Tag
for card in cards:
    try:
        title = card.find("h3").text
        link = card.find('a').get("href")
        data.append(f"{title} --- {link}\n")
    except:
        pass
    
    
result = '\n'.join(data)
if not result:
    print("we don\'t have any information about your request")
print(result)