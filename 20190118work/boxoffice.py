import csv
import requests
import json
import os
import datetime
from datetime import timedelta
from bs4 import BeautifulSoup

days = datetime.datetime(2019, 1, 20)
ago = timedelta(days=-7)
L = []
token = os.getenv("TOKEN")

with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for k in range(10):
        days = days + ago
        days_ago = days
        days_ago = days_ago.strftime('%Y%m%d')
        for i in range(10):
            url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={days_ago}&weekGb=0"
            res = requests.get(url)
            movie_list = res.json()
            movie_lists = movie_list["boxOfficeResult"]["weeklyBoxOfficeList"]
            if movie_lists[i]["movieNm"] not in L:
                L.append(movie_lists[i]["movieNm"])
                writer.writerow({'movie_code' : movie_lists[i]["movieCd"], 'title' : movie_lists[i]["movieNm"], 'audience' : movie_lists[i]["audiAcc"],'recorded_at' : days_ago})
        
with open('boxoffice.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['movie_code'], row['title'], row['audience'], row['recorded_at'])
