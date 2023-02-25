from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
db = SQLAlchemy()
api = Api(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255), nullable=True)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title} - status {self.done}>"


with app.app_context():
    db.create_all()


class TodoListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "title",
            type=str,
            required=True,
            location="json",
        )
        self.reqparse.add_argument(
            "desc",
            type=str,
            default="",
            location="json",
        )
        super(TodoListAPI, self).__init__()

    def get(self):
        tasks = Task.query.all()
        return [
            {
                "id": task.id,
                "title": task.title,
                "desc": task.desc,
            }
            for task in tasks
        ]

    def post(self):
        args = self.reqparse.parse_args()
        task = Task(title=args["title"], desc=args["desc"])
        db.session.add(task)
        db.session.commit()
        return {
            "id": task.id,
            "title": task.title,
            "desc": task.desc,
            "done": task.done,
        }


class TodoDetailAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "title",
            type=str,
            location="json",
        )
        self.reqparse.add_argument(
            "desc",
            type=str,
            location="json",
        )
        self.reqparse.add_argument(
            "done",
            type=bool,
            location="json",
        )
        super(TodoDetailAPI, self).__init__()

    def get(self, id):
        task = Task.query.get_or_404(id)
        return {
            "id": task.id,
            "title": task.title,
            "desc": task.desc,
            "done": task.done,
        }

    def put(self, id):
        args = self.reqparse.parse_args()
        task = Task.query.get_or_404(id)
        task.title = args.get("title", task.title)
        task.desc = args.get("desc", task.desc)
        task.done = args.get("done", task.done)
        db.session.commit()
        return {
            "id": task.id,
            "title": task.title,
            "desc": task.desc,
            "done": task.done,
        }

    def delete(self, id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return


api.add_resource(TodoListAPI, "/todo/tasks", endpoint="tasks")
api.add_resource(TodoDetailAPI, "/todo/tasks/<int:id>", endpoint="task")


if __name__ == "__main__":
    app.run(debug=True)
