from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<center><h1> Journey of a 1000 miles begins with a single step </h1> <center>"

if __name__ == '__main__':
    app.run(debug=True)