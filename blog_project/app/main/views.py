import datetime
import os
from flask import render_template, request, session, redirect
# 导入蓝图程序main 用于构建路由
from . import main
# 导入db 以及 models们
from .. import db
from ..models import *

# 首页的访问路由
@main.route('/')
def index_views():
    categories = Category.query.all()
    topics = Topic.query.all()
    print('这是首页的访问路由')
    # 获取登录信息
    if 'uname' in session and 'uid' in session:
        print('进入登录了')
        print(session['uname'])
        user = User.query.filter_by(id=session['uid']).first()
        print(user)
    return render_template('index.html',params=locals())

@main.route('/login',methods=['GET','POST'])
def login_v():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 接收前端传过来的数据
        loginname = request.form.get('username')
        upwd = request.form.get('password')
        #使用接收的数据去数据库验证-查询
        user = User.query.filter_by(loginname=loginname,upwd=upwd).first()
        if user:
            print('在执行将信息存入session')
            session['uid'] = user.id
            session['uname'] = user.uname
            return redirect('/')
        else:
            error_msg = '用户名或密码不正确'
            return render_template('login.html',error_msg = error_msg)

@main.route('/register')
def register_v():
    return render_template('register.html')
@main.route('/logout')
def logout_v():
    #获取源地址,有原地址的话则返回原地址,否则跳转到首页
    url = request.headers.get('referer','/')
    #判断登录信息是否在session中;
    if 'uid' in session and 'uname' in session:
        del session['uid']
        del session['uname']
    return redirect('/')

@main.route('/release',methods=['GET','POST'])
def release_v():
    if request.method == 'GET':
    # 首先判断是否有登录,是否是作者
        if 'uid' in session and 'uname' in session:
             user = User.query.filter_by(id=session.get('uid')).first()
             if user.is_author != 1:
                 return redirect('/')
             else:
                 topics = Topic.query.all()
                 categorys = Category.query.all()
                 blogtypes = BlogType.query.all()
                 return render_template('release.html',params=locals())
        else:
            return  redirect('/login')
    else:
        #将写入的信息保存进数据库
        topic = Topic()
        topic.title = request.form.get('author')
        topic.blogtype_id = request.form.get('list')
        topic.category_id = request.form.get('category')
        topic.user_id = session.get('uid')
        topic.content = request.form.get('content')
        print('topic.content:',topic.content)
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d")
        f = request.files.get('file_pics')
        if f:
            # 获取要上传的文件
            print('进入保存图片了')
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext = f.filename.split('.')[1]
            filename = ftime + '.' + ext
            topic.images = 'upload/'+filename
            # 将文件保存至服务器
            basedir = os.path.dirname(os.path.dirname(__file__))
            upload_path = os.path.join(basedir,'static/upload',filename)
            print(upload_path)
            f.save(upload_path)
        db.session.add(topic)
        return redirect('/')
@main.route('/info')
def info_v():
    pass

@main.route('/like')
def like_v():
    read_num = Topic.query.filter_by(id=14)

@main.route('/list')  #文章列表定义路径
def list_v():
    return render_template('list.html')

@main.route('/photo')   #定义照片路径
def photo_v():
    return render_template('photo.html')

@main.route('/gbook')  #定义留言路径
def gbool_v():
    return render_template('gbook.html')

@main.route('/time')   #定义时间轴路径
def time_v():
    return render_template('time.html')

@main.route('/about')  #定义关于我的路径
def about_v():
    return render_template('about.html')



