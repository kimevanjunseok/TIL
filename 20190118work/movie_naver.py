import csv
import requests
import json
import os
import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
from pprint import pprint

movie_list = []
with open('boxoffice.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_list.append(row['title'])

print(movie_list)
for i in movie_list:

    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")

    headers = {
            "X-Naver-Client-Id" : client_id,
            "X-Naver-Client-Secret" : client_secret
    }
    url = f"https://openapi.naver.com/v1/search/movie.json?query={i}"
    res = requests.get(url, headers=headers).json()
    pprint(res)
