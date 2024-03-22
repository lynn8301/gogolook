import json
from models.task import Task, db
from utlis import Utils

class TaskService():
    def __init__(self):
        pass
    
    def get_all(self):
        try:
            tasks = Task.query.all()
            tasks_data = []
            for task in tasks:
                task_data = {
                    'id': task.id,
                    'name': task.name,
                    'status': Utils.bool_show_int(task.status)
                }
                tasks_data.append(task_data)
            return tasks_data
        except Exception as e:
            print("from service - get_all")
            print(e)

    def create(self, name):
        try:
            new_task = Task(name = name)
            db.session.add(new_task)
            db.session.commit()
            task = Task.query.filter_by(name = name).order_by(Task.id.desc()).first()
            task_data = {
                'id': task.id,
                'name': task.name,
                'status': Utils.bool_show_int(task.status)
            }
            return task_data
        except Exception as e:
            print("from service - create")
            print(e)

    
    def update(self, id, update_task):
        try:
            task = db.session.get(Task, id)
            if task:
                if "name" in update_task: task.name = update_task["name"]
                if "id" in update_task: task.id = update_task["id"]
                if "status" in update_task: task.status = update_task["status"]
                db.session.commit()
            else:
                return 'id: {}  not existed'.format(id), 200
            
            task = db.session.get(Task, id)
            task_data = {
                'id': task.id,
                'name': task.name,
                'status': Utils.bool_show_int(task.status)
            }
            return task_data
        except Exception as e:
            print("from service - update")
            print(e)

    
    def delete(self, id):
        try:
            task = db.session.get(Task, id)
            if task:
                db.session.delete(task)
                db.session.commit()
                return "done"
            else:
                return 'id: {}  not existed'.format(id), 200
        except Exception as e:
            print("from service - update")
            print(e)

taskService = TaskService()