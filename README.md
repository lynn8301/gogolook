# Code Exercise

## SETUP
### Build Docker
```
docker build -t gogolook
docker run -p 8000:8000 gogolook
```

## API DOCUMENT

### 1. GET /task (list tasks)
```
{
    "result": [
        {"id": 1, "name": "name", "status": 0}
    ]
}
```
Note: Origianl document shows `GET /tasks`; however, for api consistency, we modify it as `GET /task`.

### 2. POST /task (create task)
```
request
{
    "name": "買晚餐"
}
response status code 201
{
  "result": {
    "name": "買晚餐",
    "status": 0,
    "id": 1
  }
}
```

### 3. PUT /task/<id> (update task)
```
request
{
  "name": "買早餐",
  "status": 1,
  "id": 1
}
response status code 200
{
  "result": {
    "name": "買早餐",
    "status": 1,
    "id": 1
  }
}
```

### 4. DELETE /task/<id> (delete task)
response status code 200

### What should we do next?
1. add logger
2. modify API sturcture
