from monster_class import *
from student_class import *
from teacher_class import *
from workshop_class import *
from functions import *

# Creating a student with first name and last name
student1 = Student('Bob', 'Mate', 1)
student2 = Student('Liv', 'Tree', 2)
student3 = Student('Dave', 'Ham', 3)

student_list = [student1, student2, student3]

[print(i.f_name, i.l_name) for i in student_list]

# Create teachers
teacher1 = Teacher('Sir', 'Rob', 1)
teacher2 = Teacher('Sir', 'Dirk', 2)
teacher3 = Teacher('Sir', 'Mike', 3)

teacher_list = [teacher1, teacher2, teacher3]

[print(i.f_name, i.l_name, i.staff_id) for i in teacher_list]

# Create workshop
workshop1 = monster_workshop('Scare', 'Sir Rob')
workshop2 = monster_workshop('Math', 'Sir Dirk')
workshop3 = monster_workshop('Geo', 'Sir Mike')

workshop_list = [workshop1, workshop2, workshop3]

[print(i.subject, i.teacher) for i in workshop_list]

# Add skills to student
skill_list = ['Roar', 'Wolf']
add_skills(student2, skill_list)
print(student2.skills)