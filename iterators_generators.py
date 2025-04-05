import random

class StudentList:
    def __init__(self, std_list):
        self.std_list = std_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.std_list):
            raise StopIteration
        std = self.std_list[self.index]
        self.index += 1
        return std


def attendance_generator(std_list):
    for std in std_list:
        yield (std, random.choice(["Present", "Absent"]))


def random_marks_generator(std_list, max_marks=100):
    for std in std_list:
        yield (std, random.randint(50, max_marks))


if __name__ == "__main__":
    std_list = ["Zainab", "Hassan", "Fatima", "Usman", "Areeba"]

    print("Iterating Students:")
    for std in StudentList(std_list):
        print(std)

    print("\nAttendance:")
    for std, status in attendance_generator(std_list):
        print(f"{std}: {status}")

    print("\nRandom Marks:")
    for std, marks in random_marks_generator(std_list):
        print(f"{std}: {marks}")
