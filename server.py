from flask import Flask
app = Flask(__name__)

VERSION = '3.0'

@app.route('/')
def index():
    return 'version {}'.format(VERSION)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
