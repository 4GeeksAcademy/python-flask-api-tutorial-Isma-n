from flask import  Flask, request, jsonify

app = Flask(__name__)

# Lista global de tareas
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Endpoint GET para obtener la lista
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Endpoint POST para recibir una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)