from flask import Flask
app = Flask(__name__)

VERSION = '3.2'

@app.route('/')
def index():
    return str(VERSION)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
