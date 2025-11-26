from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, CI/CD World! v2.0 - Updated!!</h1>' # <- 수정된 부분

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)