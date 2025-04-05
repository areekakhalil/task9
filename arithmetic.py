def calculate_percentage(obtained, total):
    try:
        return round((obtained / total) * 100, 2)
    except ZeroDivisionError:
        return 0

def classify_grade(percentage):
    if percentage >= 85:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'F'
