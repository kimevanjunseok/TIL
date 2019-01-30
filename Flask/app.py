from flask import Flask, render_template
import os
import datetime
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
































    
if __name__=='__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)