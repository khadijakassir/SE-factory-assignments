import json  #note that i got a lot of help from chatgpt
class Course:
    def __init__(self, code, name, credit_hours, is_core):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.is_core = is_core
    def __str__(self):
        course_type = "Core" if self.is_core else "Elective"
        return f"{self.code}: {self.name} ({self.credit_hours} credits) - {course_type}"
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = {}
    def enroll_in_course(self, course):
        if course.code in self.enrolled_courses:
            raise ValueError(f"Already enrolled in course {course.code}")
        self.enrolled_courses[course.code] = course
        print(f"Enrolled in course {course.name}")
    def drop_course(self, course_code):
        if course_code not in self.enrolled_courses:
            raise ValueError(f"Course {course_code} not found in enrollment")
        del self.enrolled_courses[course_code]
        print(f"Dropped course {course_code}")
    def list_courses(self):
        if not self.enrolled_courses:
            print("No courses enrolled.")
        else:
            for course in self.enrolled_courses.values():
                print(course)
class CourseCatalog:
    def __init__(self):
        self.courses = {}
    def add_course(self, course):
        if course.code in self.courses:
            raise ValueError(f"Course {course.code} already exists in the catalog.")
        self.courses[course.code] = course
        print(f"Course {course.name} added to catalog.")
    def get_course(self, course_code):
        if course_code not in self.courses:
            raise ValueError(f"Course {course_code} not found in catalog.")
        return self.courses[course_code]
    def save_to_file(self, filename="course_catalog.json"):
        with open(filename, "w") as file:
            json.dump({code: vars(course) for code, course in self.courses.items()}, file)
        print(f"Catalog saved to {filename}.")
    def load_from_file(self, filename="course_catalog.json"):
        with open(filename, "r") as file:
            data = json.load(file)
            for code, course_info in data.items():
                course = Course(course_info['code'], course_info['name'], course_info['credit_hours'], course_info['is_core'])
                self.courses[code] = course
        print(f"Catalog loaded from {filename}.")

def main():
    catalog = CourseCatalog()
    students = {}
    while True:
        print("\n1. Add Course\n2. Enroll Student in Course\n3. Drop Course for Student\n4. List Student Courses\n5. Save Course Catalog\n6. Load Course Catalog\n7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            code = input("Enter course code: ")
            name = input("Enter course name: ")
            credit_hours = int(input("Enter credit hours: "))
            is_core = input("Is this a core course? (yes/no): ").lower() == "yes"
            course = Course(code, name, credit_hours, is_core)
            catalog.add_course(course)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            course_code = input("Enter course code to enroll in: ")

            student = students.setdefault(student_id, Student(student_id, student_name))
            try:
                course = catalog.get_course(course_code)
                student.enroll_in_course(course)
            except ValueError as e:
                print(e)

        elif choice == "3":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code to drop: ")

            student = students.get(student_id)
            if student:
                try:
                    student.drop_course(course_code)
                except ValueError as e:
                    print(e)
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input("Enter student ID: ")
            student = students.get(student_id)
            if student:
                student.list_courses()
            else:
                print("Student not found.")

        elif choice == "5":
            catalog.save_to_file()

        elif choice == "6":
            catalog.load_from_file()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
