{"filter":false,"title":"models.py","tooltip":"/orm/models.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":42},"action":"insert","lines":["# table 만들기","class User(db.Model):","    __tablename__ = 'users'","    id = db.Column(db.Integer, primary_key=True)","    username = db.Column(db.String(80), unique=True, nullable=False)","    email = db.Column(db.String(120), unique=True, nullable=False)","    ","    def __repr__(self):","        return f\"<User '{self.username}'>\""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":39},"action":"insert","lines":["from flask_sqlalchemy import SQLAlchemy"],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":20},"action":"insert","lines":["db = SQLAlchemy(app)"],"id":5}],[{"start":{"row":2,"column":20},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"remove","lines":["p"],"id":7},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"remove","lines":["p"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["a"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":21},"end":{"row":5,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":33,"mode":"ace/mode/python"}},"timestamp":1549518363381,"hash":"0aaf87561cbddaa8c59527a659626010377f186c"}