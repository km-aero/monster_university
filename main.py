from student_class import *
from teacher_class import *
from workshop_class import *

# Initialise lists
student_list = []
teacher_list = []
workshop_list = []
skill_list = []

# Administrators Program
while True:
    try:
        print('========================Welcome Administrator========================')
        print('1: Create a student')
        print('2: Add skills to student')
        print('3: List all skills of a student')
        print('4: List all students')
        print('5: Create a teacher')
        print('6: List all teachers')
        print('7: Create a workshop')
        print('8: List all workshops')
        print('9: Exit')
        print('=====================================================================')
        menu_num = int(input('\nPlease enter the number for the above menu options (e.g. \'1\')\n'))

        if menu_num == 1:
            # Creating a student with first name and last name
            while True:
                f_name = input('Please enter the students first name or write \'exit\' to exit.\n')
                if ('exit' in f_name):
                    break
                else:
                    l_name = input('Please enter the students last name.\n')
                    i = len(student_list) + 1
                    student_list.append(Student(f_name, l_name, i))

        elif menu_num == 2:
            while True:
                skill = input('Please enter the skill you want to add or enter \'exit\' to exit to menu.\n')
                if ('exit' in skill):
                    break
                else:
                    student_id = input('Please enter the student_id for the student you wish to add skills to.\n')
                    student_list[int(student_id)-1].add_skills(skill)

        elif menu_num == 3:
            # List students skills
            while True:
                student_id = input('Please enter the student_id for the student you wish to display skills or enter ' +
                                   '\'exit\' to exit to menu.\n')
                if ('exit' in student_id):
                    break
                else:
                    if student_list[int(student_id)-1].skills == []:
                        print('No skills available.')
                        input('\nPress enter/return to continue to the menu.\n')
                    else:
                        print('Skills of', student_list[int(student_id)-1].f_name,
                              student_list[int(student_id)-1].l_name)
                        [print('-', student_list[int(student_id)-1].skills[i]) for i in
                         range(len(student_list[int(student_id)-1].skills))]
                        input('\nPress enter/return to continue to the menu.\n')

        elif menu_num == 4:
            # List all students
            print('First Name |', 'Last Name |', 'Student ID')
            [print(i.f_name, '|', i.l_name, '|', i.student_id) for i in student_list]
            input('\nPress enter/return to continue to the menu.\n')

        elif menu_num == 5:
            # Create teachers
            while True:
                f_name = input('Please enter the teachers first name or write \'exit\' to exit.\n')
                if ('exit' in f_name):
                    break
                else:
                    l_name = input('Please enter the teachers last name.\n')
                    i = len(teacher_list) + 1
                    teacher_list.append(Teacher(f_name, l_name, i))

        elif menu_num == 6:
            # List all teachers
            print('First Name |', 'Last Name |', 'Staff ID')
            [print(i.f_name, '|', i.l_name, '|', i.staff_id) for i in teacher_list]
            input('\nPress enter/return to continue to the menu.\n')

        elif menu_num == 7:
            # Create workshop
            while True:
                subject = input('Please enter the subject name or write \'exit\' to exit.\n')
                if ('exit' in subject):
                    break
                else:
                    staff_id = input('Please enter the teacher\'s ID number.\n')
                    workshop_list.append(MonsterWorkshop(subject, staff_id))

        elif menu_num == 8:
            # List all workshops
            print('First Name |', 'Staff ID')
            [print(i.f_name, '|', i.staff_id) for i in workshop_list]
            input('\nPress enter/return to continue to the menu.\n')

        elif menu_num == 9:
            print('Have a good day!')
            break

        else:
            print('Please enter a number in the menu.')
            input('\nPress enter/return to continue to the menu.\n')

    except ValueError:
        print('Please enter a number in the menu.')
        input('\nPress enter/return to continue to the menu.\n')

    except TypeError:
        print('Please enter a number in the menu.')
        input('\nPress enter/return to continue to the menu.\n')

    except IndexError:
        print('Error: Please enter a number\nYou will need to start from the main menu.')
        input('\nPress enter/return to continue to the menu.\n')