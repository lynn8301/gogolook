from flask import request, json
from models.task import Task, db
from services.taskService import taskService

class TaskController():
    def __init__(self):
        pass
    
    def get_all(self):
        try:
            result = taskService.get_all()
            response = {
                "result": result
            }
            return response
        except Exception as e:
            print("from controller - get_all")
            print(e)

    def create(self):
        try:
            req_json = request.get_json()
            name = req_json.get("name")
            result = taskService.create(name)
            response = {
                "result": result
            }
            return response, 201
        except Exception as e:
            print("from controller - create")
            print(e)

    def update(self, id):
        try:
            update_task = request.get_json()
            result = taskService.update(id, update_task)
            if result is not dict:
                return result
            response = {
                "result": result
            }
            return response
        except Exception as e:
            print("from controller - update")
            print(e)
            
    def delete(self, id):
        try:
            result = taskService.delete(id)
            return result
        except Exception as e:
            print("from controller - delete")
            print(e)

taskController = TaskController()