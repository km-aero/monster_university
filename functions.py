def modify_skill_list(student, skill):
    student.add_skills(skill)

def add_skills(student, sk_list):
    for i in sk_list:
        modify_skill_list(student, i)