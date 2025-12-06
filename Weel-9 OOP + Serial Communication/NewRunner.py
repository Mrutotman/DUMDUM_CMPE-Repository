student1_name = "Diego"
student1_grade = "1.5"
student1_subject = ["Algebra", "Physics"]

student2_name = "John"
student2_grade = "1.0"
student2_subject = ["Geometry", "Physics"]

student3_name = "Mark"
student3_grade = "2.5"
student3_subject = ["Algebra", "English"]

def print_student_info(name, grade, subject):
    print(f"{name} grade: {grade} subject: {subject}")

#if __name__ == "__main__":
    #print_student_info(student1_name, student1_grade, student1_subject)
    #print_student_info(student2_name, student2_grade, student2_subject)
    #print_student_info(student3_name, student3_grade, student3_subject)

class Student:
    defaultsub = ["CMPE", "CFE"]

    def __init__(self, name, grade, subjects):
        self.name = name
        self.grade = grade
        self.subjects = subjects

    def print_student_info(self):
        print(f"{self.name} grade: {self.grade} subject: {self.subjects}")

    @classmethod
    def create_default_student(cls, name, grade):
        return cls(name, grade, cls.defaultsub)

    @staticmethod
    def is_grade_passing(grade):
        return grade <= 3.00

# Creating objects (instances) for each student
if __name__ == "__main__":
    student1 = Student("Diego", 1.5, ["Algebra", "Physics"])
    student1.print_student_info()
    if student1.is_grade_passing(student1.grade):
        print("PASS")
    else:
        print("FAIL")

    student2 = Student.create_default_student("John", 1.0)
    student2.print_student_info()
    if student2.is_grade_passing(student2.grade):
        print("PASS")
    else:
        print("FAIL")

    student3 = Student("Mark", 2.5, ["Algebra", "English"])
    student3.print_student_info()
    if student3.is_grade_passing(student3.grade):
        print("PASS")
    else:
        print("FAIL")

    student4 = Student("Utot", 5.0, ["Recess", "Lunch"])
    student4.print_student_info()
    if student4.is_grade_passing(student4.grade):
        print("PASS")
    else:
        print("FAIL")