from flask import Flask
app = Flask(__name__)

VERSION = '1.3'

@app.route('/')
def index():
    return str(VERSION)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
