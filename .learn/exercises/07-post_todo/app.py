from flask import request, Flask, jsonify

app = Flask(__name__)

# Lista global de tareas
todos = [{"label": "My first task", "done": False}]

# Endpoint GET para obtener la lista
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Endpoint POST para recibir una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

