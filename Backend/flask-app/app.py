from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
db = SQLAlchemy()
api = Api(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255), nullable=True)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title} - status {self.done}>"


class TodoListAPI(Resource):
    def get(self):
        ...

    def post(self):
        ...


class TodoDetailAPI(Resource):
    def get(self):
        ...

    def put(self):
        ...

    def delete(self):
        ...


@app.route("/")
def hello_world():
    task = Task(title="first task", desc="zrob to i to")
    return f"<p>Hello, World!</p> {task.title} {task.desc}"


if __name__ == "__main__":
    app.run(debug=True)
