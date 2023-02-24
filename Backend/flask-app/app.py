from flask import Flask
from db import db

app = Flask(__name__)
db.init_app(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["DEBUG"] = True


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    flask.run(debug=True)
