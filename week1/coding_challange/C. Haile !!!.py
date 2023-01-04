no_of_students = int(input())
student_list = []
for i in range(no_of_students):
    student = input()
    student_list.append(student)
for i in student_list:
    student_info = i.replace('#', " ")
    print(student_info)
