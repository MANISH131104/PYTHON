class Student:


     # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    college_name = "MDU"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def hello(self):
        print("Hello Manish ! ")    

    def get_marks(self):
        return self.marks
    

s1 = Student("Manish",100)
print(s1.name,s1.marks)      # Manish
print(s1.college_name)
print(s1.get_marks())


s2 = Student("Tannu",85)
print(s2.name,s2.marks)
s2.hello()



