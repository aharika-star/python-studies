# EXERCISE 3

pending_books = []

pending_books.append("Python Basics")
pending_books.append("c")
pending_books.append("Data Science")

print("Total Books:", len(pending_books))

pending_books.pop(1)

print("Available Books:", pending_books)


# EXERCISE 4

students = [
    {"course": "Python", "name": "Harika"},
    {"course": "c", "name": "suba"},
    {"course": "Python", "name": "harina"}
]

print("\nStudents Enrolled in Python Course:")

for student in students:
    if student["course"] == "Python":
        print(student["name"])
