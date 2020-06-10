from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/01-log',methods=['POST','GET'])

def log():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        uname = request.form('[username]')
        print(uname)
        return 'ok'

if __name__ == "__main__":
    app.run(debug=True)