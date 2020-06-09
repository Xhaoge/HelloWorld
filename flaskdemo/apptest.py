from flask import Flask,make_response

app = Flask(__name__)

@app.route('/')
def hello_v():
    return 'welcome'

@app.route('/01-setcookie')
def setcookie_v():
    resp = make_response('添加cookie成功')
    resp.set_cookie('uname','sss',60*60)
    return resp

# @app.route('/get-cookie')
# def getcook_v():

# @app.route('/03-session')
# def setsession():
#     session['uname'] = 'ssss'
#     return 'ok'
#
# @app.route('/03-getsession')
# def getsession():
#     uname = session.get('uname','')
#     if uname:
#         return '用户名为:%s'%uname
#     else:
#         return '没找到相关信息'

if __name__ == '__main__':
    app.run(debug=True)