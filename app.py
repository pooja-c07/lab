from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Flask Docker Container!</h1>'

@app.route('/about')
def about():
    return '<h2>This Flask application is running inside Docker.</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)