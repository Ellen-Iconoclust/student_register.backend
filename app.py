from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend calls

students = []  # temporary in-memory database

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get("name")
    roll = data.get("roll")
    class_name = data.get("class_name")

    student = {"name": name, "roll": roll, "class_name": class_name}
    students.append(student)

    return jsonify({"message": f"Student {name} registered successfully!", "students": students})

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
