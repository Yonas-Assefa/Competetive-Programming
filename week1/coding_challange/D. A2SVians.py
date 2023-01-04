student_no = int(input())

excellent_students = student_no
student_list = set(input().split(" "))
bad_students = set(input().split(" "))

good_students = list(student_list.symmetric_difference(bad_students))
excellent_students = 0
for name in good_students:
    lower_name = name.lower()
    name_set = set(lower_name.split())
    if len(name_set) * 2 == len(lower_name):
        excellent_students += 1


    
print(excellent_students)

