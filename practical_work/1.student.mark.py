students = [] 
courses = [] 
marks = {} 

#Input functions

def input_number_students():
    return int(input("Input number of students: "))

def create_student():
    student_id = str(input("Input student id: "))

    student_name = str(input("Input student name: "))
    birthday = str(input("Input student day of birth (DD-MM-YYYY): "))
    return {'id': student_id, 'name': student_name, 'birthday': birthday}

def input_number_courses():
    return int(input("Input number of courses: "))

def create_course():
    course_id = str(input("Input course id: "))

    course_name = str(input("Input course name: "))
    return {'id': course_id, 'name': course_name}

def input_student_marks(course_id, isAll = True):

    if course_id not in [c['id'] for c in courses] and isAll == False :
        print("no have this course!")
        return

    student_mark = {}
    for student in students:
        mark = float(input(f"Input mark of {course_id} for {student['name']}: "))
        student_mark[student['id']] = mark
    marks[course_id] = student_mark

#List functions

def list_students():
    if (len(students) < 1):
        print("No student!")
        return
    print("=== Students ===")
    for student in students:
        print("Id: ", student['id'])
        print("Name: ", student['name'])
        print("Birthday: ", student['birthday'])
        print('-' * 5)

def list_courses():
    if (len(courses) < 1):
        print("No course!")
        return
    print("=== Courses ===")
    for course in courses:
        print("Id: ", course['id'])
        print("Name: ", course['name'])
        print('-' * 5)

def show_student_marks():
    if (len(marks) < 1):
        print("No students!")
    for c_id, s_map in marks.items():
        print(f'Marks for {c_id}')
        for s_id, s_mark in s_map.items():
            name = next((s['name'] for s in students if s['id'] == s_id), s_id)
            print(f"{name} - {s_id}: {s_mark}")
        print('-' * 10)
         
    
def main():
    while True:
        print("=== Menu ===")
        print("1. List students")
        print("2. List courses")
        print("3. Create student")
        print("4. Create course")
        print("5. List marks for all courses")
        print("6. Input marks in a course")
        print("7. Input marks for all courses")

        print("Choose your choice: ")
        choice = int(input("Enter: "))

        if choice == 1:
            list_students()
        elif choice == 2:
            list_courses()
        elif choice == 3:
            show_student_marks()
        elif choice == 4:
            c_id = str(input("Enter course id"))
            input_student_marks(c_id, False)
        elif choice == 5:
            for c in courses:
                input_student_marks(c['id'])
        else:
            break
    


if __name__ == "__main__":
    main()
