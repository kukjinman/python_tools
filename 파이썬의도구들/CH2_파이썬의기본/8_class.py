# 클래스를 사용하지 않은 예제
A_School = []
B_School = []

# 학생 추가 함수
def add_student(name, age, grade, school_):
    student = {'name': name, 'age': age, 'grade': grade}
    school_.append(student)

# 학생 정보 출력 함수
def print_students(school_):
    for student in school_:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# 학생 추가
add_student('John', 15, '9th', A_School)
add_student('Jane', 14, '8th', A_School)
add_student('Tom', 16, '10th', B_School)
add_student('Jerry', 15, '9th', B_School)

# 학생 정보 출력
print_students(A_School)
print_students(B_School)


# =========================================================
# 클래스를 사용한 예제


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students(self):
        for student in self.students:
            student.print_info()

# 학생 추가
A_School = School()
A_School.add_student(Student('John', 15, '9th'))
A_School.add_student(Student('Jane', 14, '8th'))

B_School = School()
B_School.add_student(Student('Tom', 16, '10th'))
B_School.add_student(Student('Jerry', 15, '9th'))

# 학생 정보 출력
A_School.print_students()
B_School.print_students()



