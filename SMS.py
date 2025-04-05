class Student:
    def __init__(self, name, age, std_id, enrolled):
        self._name = name
        self._age = age
        self._std_id = std_id
        self._enrolled = enrolled  # List of tuples: (course_name, grade)

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_std_id(self):
        return self._std_id

    def get_enrolled(self):
        return self._enrolled

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_std_id(self, std_id):
        self._std_id = std_id

    def set_enrolled(self, enrolled):
        self._enrolled = enrolled

    def calculate_gpa(self):
        if not self._enrolled:
            return 0.0
        total = sum(grade for course, grade in self._enrolled)
        return round(total / len(self._enrolled), 2)


class GraduateStudent(Student):
    def __init__(self, name, age, std_id, enrolled, thesis):
        super().__init__(name, age, std_id, enrolled)
        self._thesis = thesis

    def __str__(self):
        return f"Graduate Student: {self.get_name()}, Age: {self.get_age()}, ID: {self.get_std_id()}, Thesis: {self._thesis}, GPA: {self.calculate_gpa()}"


if __name__ == "__main__":
    std = GraduateStudent("Ali", 24, "CS001", [("Math", 3.5), ("AI", 3.8)], "AI in Education")
    print(std)
