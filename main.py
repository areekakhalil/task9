from student_utils.arithmetic import calculate_percentage, classify_grade
from student_utils.attendance import attendance_percentage
from student_utils.performance import is_top_performer, is_probation

if __name__ == "__main__":
    print("Percentage:", calculate_percentage(450, 500))
    print("Grade:", classify_grade(88))

    print("Attendance:", attendance_percentage(42, 48))

    print("Top Performer:", is_top_performer(3.8))
    print("On Probation:", is_probation(1.9))
