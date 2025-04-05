def read_students_file(file_name):
    try:
        with open(file_name, 'r') as f:
            std_list = f.readlines()
            print("Student Records:")
            for std in std_list:
                print(std.strip())
            print(f"Total Students: {len(std_list)}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error reading file:", e)


def write_students_file(out_file, std_data):
    try:
        with open(out_file, 'w') as f:
            for std in std_data:
                f.write(std + "\n")
        print(f"Data written to {out_file}")
    except Exception as e:
        print("Error writing file:", e)


if __name__ == "__main__":
    read_students_file("students.txt")
    sample_data = [
        "Zainab, 21, BSCS01, DSA|3.7, OOP|3.9, DBMS|3.6",
        "Hassan, 22, BSCS02, DLD|3.4, SE|3.2, AI|3.8",
        "Fatima, 20, BSCS03, PF|3.9, OOP|4.0, OS|3.5",
        "Usman, 23, BSCS04, CN|3.3, DBMS|3.4, WEB|3.6",
        "Areeba, 21, BSCS05, AI|3.9, ML|3.8, NLP|3.7"
    ]
    write_students_file("student_output.txt", sample_data)
