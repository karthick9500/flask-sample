from pymongo import MongoClient
client = MongoClient('localhost', 27017,username='admin',
                     password='admin',)

db = client.flask_db
todos = db.todos
print(todos)