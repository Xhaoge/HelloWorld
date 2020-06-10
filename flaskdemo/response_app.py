from flask import Flask,render_template,request,make_response,redirect
import os
import datetime
app = Flask(__name__)

@app.route('/01-res')

def response_views():
    resp = make_response('响应内容')
    return resp

@app.route('/02-reid')
def reid_view():
    return redirect('/01-res')

@app.route('/03-file',methods=['GET','POST'])
def file_v():
    if request.method == 'GET':
        return render_template('05-file.html')
    else:
        # 接收上传的文件,保存至指定的目录处
        f = request.files['uimg']
        ftime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        ft = f.filename.split('.')[1]
        ff = f.filename.split('.')[0]
        filename = ff+ftime+'.'+ft
        # 当前.py文件的绝对地址
        based = os.path.dirname(__file__)
        uploadd = os.path.join(based,'static/')
        print(ftime)
        print(based,uploadd)
        print(f)
        print(filename)
        f.save(uploadd+filename)
        return 'ok'


if __name__ == "__main__":
    app.run(debug=True)