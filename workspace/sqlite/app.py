from flask import Flask, render_template, request, redirect
import os
import datetime
import requests
from bs4 import BeautifulSoup
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!!!'
    
# 5월 20일부터 d-day 카운트출력
@app.route('/dday')
def dday():
    a = datetime.datetime(2019, 5, 20) - datetime.datetime.now()
    return f'{a.days}일 남았습니다.'
    
# variable routing
@app.route('/hi/<string:name>')
def greeting(name):
    return render_template('greeting.html', my_name=name)

@app.route('/cube/<int:number>')
def num(number):
    return f'{number}의 3제곱은 {number**3}입니다!!!!!!!'
    
# 반복문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한타인']
    return render_template('movie.html', movies=movies)

# fake google
@app.route('/google')
def google():
    return render_template('google.html')

#GET방식
@app.route('/ping')
def ping():
    return render_template('ping.html')
    
@app.route('/pong')
def pong():
    # request.args 딕셔너리
    pingpong = request.args.get('q') # html의 있는 name이랑 같아야 함 q는 key값이라 생각하면됨
    msg = request.args.get('msg')
    return render_template('pong.html', html_pingpong=pingpong, html_msg=msg)

#POST방식 (정보 X)
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')
    
@app.route('/pong_new', methods=['POST'])
def pong_new():
    name = request.form.get('q')
    msg = request.form.get('msg')
    return render_template('pong_new.html', html_pingpong=name, html_msg=msg)
    
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)

# CSV
@app.route('/timeline')
def timeline():
    with open('timeline.csv', newline='', encoding='utf-8') as csvfile:
        readers = csv.DictReader(csvfile)
        reader = []
        for row in readers:
            reader.append((row))

    return render_template('timeline.html', reader=reader)
    
@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'username': username, 'message': message})
    return redirect('/timeline')
    # return render_template('timeline_create.html', username=username, message=message)
    

    
    
    
    
    
    
    
    
    
if __name__=='__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)