

students = ["Harika", "suba", "harina"]

print("FOR LOOP OUTPUT")
for student in students:
    print("Student:", student)


subjects = ["Maths", "Science", "English"]

print("ENUMERATE OUTPUT")
for index, subject in enumerate(subjects, start=1):
    print(f"{index}. {subject}")



count = 0
max_students = 3

print("WHILE LOOP OUTPUT")
while count < max_students:
    print(f"Marking Attendance for Student #{count + 1}")
    count += 1

print("Attendance Completed")
