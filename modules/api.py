# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
from app import app
from flask import jsonify
from modules.mdb import todos

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  print(todos)
  todos.insert_one({'content': "te", 'degree': "degree"})
  return jsonify({"message":"Hello from Flask!"})
