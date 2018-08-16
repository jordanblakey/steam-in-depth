from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
  return "<h2>Home Page</h2>"


@app.route("/about")
def about():
  return "<h2>About Page</h2>"


if __name__ == '__main__':
  app.run(debug=True)