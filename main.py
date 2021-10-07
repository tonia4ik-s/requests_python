from flask import Flask, jsonify, request
from entities.student_entity import Student

app = Flask(__name__)
students_data_base = [Student("Petrov", 18), Student("Diabchyk", 19)]


@app.route("/students", methods=["GET"])
def get_students():
    response_body = list(map(lambda std: {"full_name": std.full_name, "age": std.age}, students_data_base))
    return jsonify(response_body)


@app.route("/get-students", methods=["POST"])
def create_student():
    request_body = request.json
    received_students = []

    for r in request_body:
        student = Student(r["fullName"], r["age"])
        received_students.append(student)
        students_data_base.append(student)

    write_all_entities_in_file(received_students, "a")
    return_set = list_to_json(received_students)

    return jsonify(return_set)


def write_all_entities_in_file(data_base, mode):
    with open("students_data.txt", mode) as f:
        for student in data_base:
            f.write(student.to_string() + "\n")


def list_to_json(entities_list):
    entities_set = []
    for student in entities_list:
        entities_set.append(student.to_json())
    return entities_set


if __name__ == "__main__":
    write_all_entities_in_file(students_data_base, "w")
    app.run("0.0.0.0", port=3333)
