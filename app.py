from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend calls

# Preloaded 80 students with unique names, rolls, classes
all_students = [
    {"name": "Alice Smith", "roll": "101", "class_name": "10A"},
    {"name": "Bob Johnson", "roll": "102", "class_name": "10A"},
    {"name": "Charlie Brown", "roll": "103", "class_name": "10B"},
    {"name": "Diana White", "roll": "104", "class_name": "10B"},
    {"name": "Ellen Icon", "roll": "105", "class_name": "10C"},
    {"name": "Fiona Clark", "roll": "106", "class_name": "10C"},
    {"name": "George Lewis", "roll": "107", "class_name": "10D"},
    {"name": "Hannah Walker", "roll": "108", "class_name": "10D"},
    {"name": "Ian Hall", "roll": "109", "class_name": "10E"},
    {"name": "Julia Allen", "roll": "110", "class_name": "10E"},
    {"name": "Kevin Young", "roll": "111", "class_name": "10A"},
    {"name": "Laura King", "roll": "112", "class_name": "10A"},
    {"name": "Michael Wright", "roll": "113", "class_name": "10B"},
    {"name": "Natalie Scott", "roll": "114", "class_name": "10B"},
    {"name": "Oliver Green", "roll": "115", "class_name": "10C"},
    {"name": "Paula Adams", "roll": "116", "class_name": "10C"},
    {"name": "Quentin Baker", "roll": "117", "class_name": "10D"},
    {"name": "Rachel Nelson", "roll": "118", "class_name": "10D"},
    {"name": "Samuel Carter", "roll": "119", "class_name": "10E"},
    {"name": "Tina Mitchell", "roll": "120", "class_name": "10E"},
    {"name": "Ulysses Perez", "roll": "121", "class_name": "10A"},
    {"name": "Victoria Roberts", "roll": "122", "class_name": "10A"},
    {"name": "William Turner", "roll": "123", "class_name": "10B"},
    {"name": "Xavier Phillips", "roll": "124", "class_name": "10B"},
    {"name": "Yvonne Campbell", "roll": "125", "class_name": "10C"},
    {"name": "Zachary Parker", "roll": "126", "class_name": "10C"},
    {"name": "Amber Evans", "roll": "127", "class_name": "10D"},
    {"name": "Brandon Edwards", "roll": "128", "class_name": "10D"},
    {"name": "Catherine Collins", "roll": "129", "class_name": "10E"},
    {"name": "Daniel Stewart", "roll": "130", "class_name": "10E"},
    {"name": "Elena Sanchez", "roll": "131", "class_name": "10A"},
    {"name": "Frank Morris", "roll": "132", "class_name": "10A"},
    {"name": "Grace Rogers", "roll": "133", "class_name": "10B"},
    {"name": "Henry Reed", "roll": "134", "class_name": "10B"},
    {"name": "Isla Cook", "roll": "135", "class_name": "10C"},
    {"name": "Jack Morgan", "roll": "136", "class_name": "10C"},
    {"name": "Kara Bell", "roll": "137", "class_name": "10D"},
    {"name": "Liam Murphy", "roll": "138", "class_name": "10D"},
    {"name": "Maya Bailey", "roll": "139", "class_name": "10E"},
    {"name": "Nathan Rivera", "roll": "140", "class_name": "10E"},
    {"name": "Olivia Cooper", "roll": "141", "class_name": "10A"},
    {"name": "Peter Richardson", "roll": "142", "class_name": "10A"},
    {"name": "Queen Simmons", "roll": "143", "class_name": "10B"},
    {"name": "Ryan Foster", "roll": "144", "class_name": "10B"},
    {"name": "Sophia Howard", "roll": "145", "class_name": "10C"},
    {"name": "Thomas Ward", "roll": "146", "class_name": "10C"},
    {"name": "Uma Cox", "roll": "147", "class_name": "10D"},
    {"name": "Victor Diaz", "roll": "148", "class_name": "10D"},
    {"name": "Wendy Richardson", "roll": "149", "class_name": "10E"},
    {"name": "Xander Wood", "roll": "150", "class_name": "10E"},
    {"name": "Yara Hughes", "roll": "151", "class_name": "10A"},
    {"name": "Zane Watson", "roll": "152", "class_name": "10A"},
    {"name": "Aaron Brooks", "roll": "153", "class_name": "10B"},
    {"name": "Bella Sanders", "roll": "154", "class_name": "10B"},
    {"name": "Caleb Price", "roll": "155", "class_name": "10C"},
    {"name": "Daisy Bennett", "roll": "156", "class_name": "10C"},
    {"name": "Eli Barnes", "roll": "157", "class_name": "10D"},
    {"name": "Faith Wood", "roll": "158", "class_name": "10D"},
    {"name": "Gavin Ross", "roll": "159", "class_name": "10E"},
    {"name": "Hailey Henderson", "roll": "160", "class_name": "10E"},
    {"name": "Isaac Coleman", "roll": "161", "class_name": "10A"},
    {"name": "Jade Jenkins", "roll": "162", "class_name": "10A"},
    {"name": "Kyle Perry", "roll": "163", "class_name": "10B"},
    {"name": "Lily Powell", "roll": "164", "class_name": "10B"},
    {"name": "Mason Patterson", "roll": "165", "class_name": "10C"},
    {"name": "Nina Long", "roll": "166", "class_name": "10C"},
    {"name": "Owen Hughes", "roll": "167", "class_name": "10D"},
    {"name": "Penelope Flores", "roll": "168", "class_name": "10D"},
    {"name": "Quinn Price", "roll": "169", "class_name": "10E"},
    {"name": "Ruby Griffin", "roll": "170", "class_name": "10E"},
    {"name": "Sean Lee", "roll": "171", "class_name": "10A"},
    {"name": "Taylor Kelly", "roll": "172", "class_name": "10A"},
    {"name": "Umar Howard", "roll": "173", "class_name": "10B"},
    {"name": "Vera Cruz", "roll": "174", "class_name": "10B"},
    {"name": "Willow Foster", "roll": "175", "class_name": "10C"},
    {"name": "Ximena Powell", "roll": "176", "class_name": "10C"},
    {"name": "Yusuf Griffin", "roll": "177", "class_name": "10D"},
    {"name": "Zoey Ross", "roll": "178", "class_name": "10D"},
    {"name": "Adam Kim", "roll": "179", "class_name": "10E"},
    {"name": "Bianca Ward", "roll": "180", "class_name": "10E"},
]

present_students = []  # stores students marked present

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get("name")
    roll = data.get("roll")
    class_name = data.get("class_name")

    # Check against preloaded students
    for student in all_students:
        if (
            student["name"].lower() == name.lower()
            and student["roll"] == roll
            and student["class_name"].lower() == class_name.lower()
        ):
            # Already marked present?
            for p in present_students:
                if p["roll"] == roll:
                    return jsonify({"message": f"{name} is already marked present!"}), 400
            present_students.append(student)
            return jsonify({"message": f"Welcome {name}, you are marked present!"})

    return jsonify({"message": "Invalid entry, student not found!"}), 400

# Admin route
ADMIN_NAME = "admin"
ADMIN_CODE = "9999"  # secret code

@app.route('/admin', methods=['POST'])
def admin():
    data = request.get_json()
    name = data.get("name")
    code = data.get("code")

    if name.lower() == ADMIN_NAME and code == ADMIN_CODE:
        return jsonify({
            "message": "Admin access granted",
            "present_students": present_students
        })
    else:
        return jsonify({"message": "Unauthorized access!"}), 401

@app.route('/')
def home():
    return "Backend is running with 80 students preloaded!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

