import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from route.task import task
from models.task import db

db_name = 'data.sqlite'
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def hello_world():
    return 'Hello, World!'

app.register_blueprint(task, url_prefix="/task")

migrate = Migrate(app, db)
if __name__ == '__main__':  # Running the app
    app.run(host="0.0.0.0", port=8000, debug=True)
