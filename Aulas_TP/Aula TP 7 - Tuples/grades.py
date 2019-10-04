def studentId(element):
    return int(element[1][2:])

def studentName(element):
    return element[0]

def studentGrade(element):
    return sum(element[2])

def sort_grades(records):
    records = list(records)
    records.sort(key=studentId)
    records.sort(key=studentName)
    records.sort(key=studentGrade, reverse=True)
    return tuple(records)
