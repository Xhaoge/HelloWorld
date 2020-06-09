from flask import Flask,render_template,request

app = Flask(__name__)

# @app.route('/index')
#
# def index():
#     print(dir(request))
#     # 获取请求方案
#     res = request.scheme
#     #获取请求方式
#     meth = request.method
#     # 获取get方式请求数据
#     reget = request.args
#     # post请求数据
#     repo = request.form
#     # 获取cookies 中的新;获取请求路径;带参数的请求路径;完整路径;请求消息头;
#     reco = request.cookies
#     repa = request.path
#     refu = request.full_path
#     reu = request.url
#     rehe = request.headers
#     return render_template('02-re.html',params = locals())
#
# @app.route('/05-form')
# def form_get():
#     return render_template('05-form.html')
#
#
# @app.route('/06-get')
# def get_for():
#     print(request.args)
#     uname = request.args['uname']
#     upwd = request.args['upwd']
#     print(uname,upwd)
#     return  '200'

@app.route('/07-form')
def form_post():
    return render_template('07-form-post.html')

@app.route('/07-post',methods=['POST'])
def post_v():
    uname = request.form['uname']
    passwo = request.form['upwd']
    print(uname,passwo)
    return 'ok'

if __name__ == "__main__":
    app.run(debug=True)