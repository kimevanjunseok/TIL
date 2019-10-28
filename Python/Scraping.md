# Scraping

#### 설치

```bash
$ pip install requests
$ pip install bs4
```

> scraping은 많이 해봐야 익숙해지며 사람마다 불러오는 곳이 다를 수 있다.

#### scraping 방법(크롬)

> 네이버 인기순위

F12를 누르고 Ctrl + Shift + C 상태에서  

![캡처](https://user-images.githubusercontent.com/45934117/67656369-f3ab2100-f996-11e9-8950-4bb925fdcf4a.PNG)

이부분을 클릭하면

##### 

![캡처](https://user-images.githubusercontent.com/45934117/67656240-92834d80-f996-11e9-8f49-37c67b45deea.PNG)

이와 같이 나온다.

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.ah_l .ah_item'):
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print('{}는 {} 입니다.'.format(rank, name))
```

> 네이버 금융 코스피

![캡처](https://user-images.githubusercontent.com/45934117/67657086-0a527780-f999-11e9-91a4-4e27dde91f71.PNG)

같은 방식으로 클릭하면 정보가 나오며 원하는 정보를 타고 들어가면 된다.

```python
url = "https://finance.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.kospi_area .heading_area'):
    name = tag.select_one('.blind').text
    number = tag.select_one('.num').text
    print('{}는 {} 입니다.'.format(name, number))
```

> 네이버 환율

```python
url = "https://m.stock.naver.com/marketindex/index.nhn"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.stock_dn'): # 떨어진 환율 / 올라간 환율(.stock_up)
    name = tag.select_one('.stock_item').text
    number = tag.select_one('.stock_price').text
    print('{}의 환율은 {} 입니다.'.format(name, number))
```

