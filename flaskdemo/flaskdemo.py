from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import or_, func

pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost:3306/flask"

db = SQLAlchemy(app)
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    age = db.Column(db.Integer,nullable=True)
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return '<Users:%r>'%self.username

@app.route('/indext',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return  render_template('05-file.html')
    else:
        name_test = request.form['uname']
        age_test = request.form['uage']
        email_test = request.form['uemail']
        users = Users(name_test,age_test,email_test)
        db.session.add(users)
        db.session.commit()
        return  '000000'
@app.route('/01-query')
def query_v():
    users = db.session.query(Users).all()
    print(users)
    for user in users:
        print("姓名:%s,年龄:%d,邮箱:%s" % (user.username,user.age,user.email))
    # 年龄大于30的人
    # result = db.session.query(Users).filter(Users.age>30).all()
    # 年龄大于30,id大于2
    # result = db.session.query(Users).filter(Users.age>30,Users.id>2).all()
    # or_()的用法
    # result = db.session.query(Users).filter(or_(Users.age>30,Users.id>2)).all()
    # 查询所有年龄的总和
    # result = db.session.query(Users.id,func.sum(user.age)).all()
    # 查询限制行数,从第二条开始显示
    result = db.session.query(Users).limit(2).offset(1).all()
    print(result)
    return render_template('change.html',users=users)

@app.route('/del')
def del_v():
    users = db.session.query(Users).all()
    return render_template('05-file.html',users=users)

if __name__ == '__main__':
    app.run(debug = True)