from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h1>Hello, ''' + '''</h1>
      </body>
    </html>
    '''

@app.route("/status")
def status():
    return {
        'status':True,
        'name':'Motivate me!',
        'time':datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }

@app.route("/send", methods=['POST'])
def send():
    print(request.json())
    return{'ok':True}


app.run()