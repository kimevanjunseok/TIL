import requests
from bs4 import BeautifulSoup

# url = "https://www.naver.com/"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')


# for tag in soup.select('.ah_l .ah_item'):
#     rank = tag.select_one('.ah_r').text
#     name = tag.select_one('.ah_k').text
#     print(f'{rank}는 {name} 입니다.')

# url = "https://www.naver.com/"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')


# for tag in soup.select('.ah_l .ah_item'):
#     rank = tag.select_one('.ah_r').text
#     name = tag.select_one('.ah_k').text
#     print('{}는 {} 입니다.'.format(rank, name))

# url = "https://m.stock.naver.com/marketindex/index.nhn"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')

# for tag in soup.select('.international_lst .stock_up'):
#     name = tag.select_one('.stock_item').text
#     number = tag.select_one('.stock_price').text
#     print('{}의 환율은 {} 입니다.'.format(name, number))

# url = "https://m.stock.naver.com/marketindex/index.nhn"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')

# for tag in soup.select('#marketindexLastList > li'):
#     name = tag.select_one('.stock_item').text
#     number = tag.select_one('.stock_price').text
#     print('{}의 환율은 {} 입니다.'.format(name, number))

# for tag in soup.select('.stock_dn'):
#     name = tag.select_one('.stock_item').text
#     number = tag.select_one('.stock_price').text
#     print('{}의 환율은 {} 입니다.'.format(name, number))


# url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')

# for tag in soup.select('.link'):
#     country = tag.select_one('.name').text
#     number = tag.select_one('.idx').text    
#     print('{}의 환율은 {} 입니다.'.format(country, number))

# url = "http://www.op.gg/summoner/userName=%EB%B9%A8%EA%B0%84%EB%B9%84%ED%96%89%EA%B8%B0"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')

# for tag in soup.select('.SummonerLayout'):
#     ranknumber = tag.select_one('.tierRank').text
#     print('환율은 {} 입니다.'.format(ranknumber))