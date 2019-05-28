import csv
import requests
import json
import os
from bs4 import BeautifulSoup   
from pprint import pprint

movie_list = []
movie_code = []
with open('boxoffice.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_list.append(row['title'])
        movie_code.append(row['movie_code'])

with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movie_code', 'thumb_url', 'link_url', 'user_rating')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(len(movie_list)):

        client_id = os.getenv("NAVER_CLIENT_ID")
        client_secret = os.getenv("NAVER_CLIENT_SECRET")

        headers = {
                "X-Naver-Client-Id" : client_id,
                "X-Naver-Client-Secret" : client_secret
        }
        url = "https://openapi.naver.com/v1/search/movie.json?query={0}".format(movie_list[i])
        res = requests.get(url, headers=headers).json()
        writer.writerow({'movie_code' : movie_code[i], 'thumb_url' : res['items'][0]['image'], 'link_url' : res['items'][0]['link'],'user_rating' : res['items'][0]['userRating']})

with open('movie_naver.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['movie_code'], row['thumb_url'], row['link_url'], row['user_rating'])