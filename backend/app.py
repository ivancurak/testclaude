from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for demo purposes
tasks = [
    {"id": 1, "title": "Learn React", "completed": False},
    {"id": 2, "title": "Build Flask API", "completed": False},
    {"id": 3, "title": "Connect Frontend and Backend", "completed": False}
]

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "message": "Flask backend is running!"})

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title", ""),
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = data.get('completed', task['completed'])
            task['title'] = data.get('title', task['title'])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
