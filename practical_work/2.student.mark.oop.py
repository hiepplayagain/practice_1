from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def input(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

class Student(Entity):
    def __init__(self):
        self._id = None
        self._name = None
        self._dob = None
    
    def input(self):
        self._id = int(input("ID: "))
        self._name = input("Name: ")
        self._dob = input('Date of birth: ')
    
    def display(self):
        print(f"Id: {self._id}| Name: {self._name}| DoB: {self._dob}")

class Course(Entity):
    def __init__(self):
        self._id = None
        self._name = None
    
    def input(self):
        self._id = int(input(f"ID:"))
        self._name = input("Name: ")
    
    def display(self):
        print(f"Id: {self._id}| Name: {self._name}")

class Mark(Entity):
    def __init__(self):
        self._mark = {}
    
    def input(self, students, courses):
        for course in courses:
            print(f"\nEnter mark for course: {course._name}")
            self._mark[course._id] = {}

            for student in students:
                mark = float(input(f"Mark for {student._name}: "))
                self._mark[course._id][student._id] = mark
    
    def display(self):
        print("=== Mark lists ===")

        for course_id, student_marks in self._mark.items():
            print(f"Course ID: {course_id}")
            for student_id, mark in student_marks.items():
                print(f"Student {student_id}: {mark}")

class Manager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()
    
    def input_students(self):
        n = int(input("Input number students: "))

        for i in range(n):
            print(f"Student {i + 1}: ")
            s = Student()
            s.input()
            self.students.append(s)

    def add_student(self):
        i = len(self.students)
        print(f"Student {i + 1}: ")
        s = Student()
        s.input()
        self.students.append(s)

    def input_course(self):
        n = int(input("Input number courses: "))

        for i in range(n):
            print(f"Course {i + 1}: ")
            c = Course()
            c.input()
            self.courses.append(c)

    def add_course(self):
        i = len(self.courses)
        print(f"Course {i + 1}: ")
        c = Course()
        c.input()
        self.courses.append(c)

    def list_students(self):
        if not self.students:
            print("No student! You need to add one or more students first!")
            return
        for s in self.students:
            s.display()

    def list_courses(self):
        if not self.courses:
            print("No course! You need to add one or more courses first!")
            return
        for c in self.courses:
            c.display()

    def input_mark(self):
        self.marks.input(self.students, self.courses)

    def list_marks(self):
        self.marks.display()        

def main():
    print("======= Menu ====== ")
    print("1. Add many students")
    print("2. Add a student")
    print("3. Add many courses")
    print("4. Add a course")
    print("5. List all students")
    print("6. List all courses")
    print("7. Input mark for all courses")
    print("8. Input mark for a course")
    print("9. List all marks")
    print("10. List all marks of a course")
    print("====================")

    manager = Manager()
    while True:
        choice = int(input("Your choice: "))
        if choice == 1:
            manager.input_students()

        elif choice == 2:
            manager.add_student()

        elif choice == 3:
            manager.input_course()

        elif choice == 4:
            manager.add_course()

        elif choice == 5:
            manager.list_students()

        elif choice == 6:
            manager.list_courses()

        elif choice == 7:
            manager.input_mark()

        elif choice == 8:
            print("The function is updating! It will be available!")

        elif choice == 9:
            manager.list_marks()

        elif choice == 10:
            print("The function is updating! It will be available!")

        else:
            print("Not have this command! Retry!")

if __name__ == "__main__":
    main()