import requests
from bs4 import BeautifulSoup

# url = "https://www.naver.com/"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')


# for tag in soup.select('.ah_l .ah_item'):
#     rank = tag.select_one('.ah_r').text
#     name = tag.select_one('.ah_k').text
#     print(f'{rank}는 {name} 입니다.')

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')


for tag in soup.select('.ah_l .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print('{}는 {} 입니다.'.format(rank, name))
