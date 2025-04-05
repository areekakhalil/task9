def attendance_percentage(present, total_classes):
    try:
        return round((present / total_classes) * 100, 2)
    except ZeroDivisionError:
        return 0
