from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista global de tareas
todos = [{"label": "My first task", "done": False}]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)

    todos.append(request_body)

    return jsonify(todos)
