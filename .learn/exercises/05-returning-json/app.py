from flask import Flask, jsonify

app = Flask(__name__)

todos = [{"label": "My first task", "done": False}]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)
