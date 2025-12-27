class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
    
    @staticmethod
    def create_table(n):
        students = []
        for i in range(n):
            print(f"\nEnter student {i+1}: ")
            id = int(input("Id: "))
            name = input("Name: ")
            dob = input("Date of birth: ")
            students.append(Student(id, name, dob))
        return students

    @staticmethod
    def list(students):
        print("\n=== STUDENT LIST ===")
        for s in students:
            print(f"ID: {s.id} | Name: {s.name} | DOB: {s.dob}")


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create_table(n):
        courses = []
        for i in range(n):
            print(f"\nEnter course {i+1}: ")
            id = int(input("Id: "))
            name = input("Name: ")
            courses.append(Course(id, name))
        return courses

    @staticmethod
    def list(courses):
        print("\n=== COURSE LIST ===")
        for c in courses:
            print(f"ID: {c.id} | Name: {c.name}")


class Mark:
    def __init__(self):
        self.marks = {}

    def add_mark(self, students, courses):
        for course in courses:
            print(f"Enter marks for course: {course.name}")
            mark_students = {}

            for student in students:
                mark = float(input(f"Enter mark for {student.name}: "))
                mark_students[student.id] = mark

            self.marks[course.id] = mark_students

    def list(self):
        print("=== Marks ===")
        for course_id, student_marks in self.marks.items():
            print(f"Course ID: {course_id}")
            for student_id, mark in student_marks.items():
                print(f"  Student {student_id}: {mark}")


def main():
    n_st = int(input("Enter number of students: "))
    students = Student.create_table(n_st)

    n_co = int(input("\nEnter number of courses: "))
    courses = Course.create_table(n_co)

    Student.list(students)
    Course.list(courses)

    marks = Mark()
    marks.add_mark(students, courses)
    marks.list()


if __name__ == '__main__':
    main()
