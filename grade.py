student = []
grades = []

def add_student(name,grade):
    student.append(name)
    grades.append(grade)
    
def update_student(name,garde):
    if name in student:
        index = student.index(name)
        grades(index) = grades
    else:
        print("student not found")
        
def remove_student(name):
        if name in student:
            index = student.index(name)
            student.pop(index)
            grades.pop(index)
            
        else:
            print("student not found")
            