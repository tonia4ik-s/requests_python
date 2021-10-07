class Student:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def to_string(self):
        return "Name: " + self.full_name + ", Age: " + str(self.age)

    def to_json(self):
        return {"fullName": self.full_name, "age": self.age}
