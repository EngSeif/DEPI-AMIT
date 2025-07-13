from User import User

class Student(User):
    
    def __init__(self, name, grade_level):
        super().__init__(name, "student")
        self.grade_level = grade_level
    
    def get_role(self):
        return "Student User"