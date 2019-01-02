from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800, 838), 8)
for number in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={number}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    lucky = soup.select(".ball_645")
    print(f'{number}회차 당첨번호')
    for i in lucky:
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()

# https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=837
# requests
# BeautifulSoup
# select
# print 몇회차 당첨번호

# 100회차 당첨번호
# 1 12 3 4 5 7 