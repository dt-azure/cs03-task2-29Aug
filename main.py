class Course:
    def __init__(self, id, name, format, fee):
        self.id = id
        self.name = name
        self.format = format
        self.fee = fee

    def showInfo(self):
        print(f"Course details:")
        print(f"- Course ID: {self.id}")
        print(f"- Course name: {self.name}")
        print(f"- Course format: {self.format}")
        print(f"- Course fee: VND {self.fee:,.2f}")
    
class Student:
    def __init__(self, id, name, birthday, courses=None):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.courses = courses if courses is not None else []

    def registerCourse(self, course):
        # Check if arg is a valid instance of Course class
        if not isinstance(course, Course):
            print("Invalid course input.")
            return
        
        if len(self.courses) != 0:
            # Check if course has been registered
            for i in self.courses:
                if course.id == i.id:
                    print("Course has already been registered.")
                    return
                
        self.courses.append(course)
        print("Course has been registered successfully.")
        return
    
    def showCourses(self):
        print(f"Student: {self.name}")
    
        if len(self.courses) == 0:
            print("No course registered.")
            return
        
        print(f"Number of course(s) registered: {len(self.courses)}")
        print("List of registered course(s):")
        for i, course in enumerate(self.courses):
            print(f"Course #{i + 1}:")
            course.showInfo()
        
def main():
    course1 = Course(1, "NodeJS Fullstack", "Full time", 99999000)
    course2 = Course(2, "Computer Science", "Part time", 88999000)

    
    course1.showInfo()
    print("\n")
    course2.showInfo()
    
    print("-----------------")
    
    student1 = Student(1, "Joe", "01/01/1999")
    student2 = Student(2, "Bob", "02/02/1990")

    student1.showCourses()
    print("\n")
    
    print("-----------------")

    student1.registerCourse(course1)
    student1.registerCourse({"id": 1, "name": "NodeJS Fullstack", "format": "Full time", "fee": 99999000})
    student1.registerCourse(course1)

    student2.registerCourse(course1)
    student2.registerCourse(course2)
    

    print("-----------------")
    print("\n")

    student1.showCourses()
    print("\n")
    student2.showCourses()

if __name__ == "__main__":
    main()