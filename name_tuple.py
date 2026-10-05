# Named Tuple in Python
student = ("Tomal", 24, "CSE")

print(student[0])
print(student[1])
print(student[2])

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "department"])

student = Student("Tomal", 24, "CSE")

print(student.name)
print(student.age)
print(student.department)


from collections import namedtuple


Laptop = namedtuple("Laptop", ["name", "ram", "price"])
laptop = Laptop("Hp", "16gb", 20000)

# print(laptop.price)
# print(laptop.name)
# print(laptop.ram)

Book = namedtuple("Book", ["name", "writer", 'price'])
book = Book('Obokkoikal', 'Asif Adnam', 450)

print(book.name)
print(book.writer)
print(book.price)


import keyword

print(keyword.kwlist) # check keyword list

print(keyword.iskeyword("is"))
print(keyword.iskeyword("class"))
print(keyword.iskeyword("Orrange"))

# def = 5;#its occurs the syntax error
# print(def) #


