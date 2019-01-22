import csv
import requests
import json
import os
from bs4 import BeautifulSoup   
from pprint import pprint

movie_img = []
with open('movie_naver.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_img.append(row['thumb_url'])
os.mkdir("C:/TIL_home/images")
os.chdir("C:/TIL_home/images")
for i in movie_img:
    res = requests.get(i).content
    filename = os.path.basename(i)
    with open(filename, 'wb') as f: 
        f.write(res)

