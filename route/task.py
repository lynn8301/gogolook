from flask import Blueprint, request, json
from models.task import db
from controllers.taskController import taskController

task = Blueprint('task', __name__)
task.route('', methods=['GET'])(taskController.get_all)
task.route('', methods=['POST'])(taskController.create)
task.route('/<id>', methods=['PUT'])(taskController.update)
task.route('/<id>', methods=['DELETE'])(taskController.delete)