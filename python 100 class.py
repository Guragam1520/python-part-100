class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
    
    def printAll(self):
        print(self.name,end=" " )
        print(self.age,end=" " )
        print(self.gender,end=" " )
        print(self.level,end=" " )
        print(self.grades,end=" " )



# Define some students
john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
john.printAll()
print(john.getGPA())
jane.printAll()
print(jane.getGPA())
