from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(225), index = True)
    status = db.Column(db.Boolean, default = False, nullable = False)
    
