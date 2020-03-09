from monster_class import *

class Student(Monster):
    def __init__(self,f_name, l_name, student_id):
        super().__init__(f_name, l_name, skills=[])
        self.student_id = student_id

    def add_skills(self, skills):
        self.skills.append(skills)
