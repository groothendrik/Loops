#While loops
#My way(also works)

"""all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []
index = 0

while index <= len(all_students):
  students_in_poetry = all_students.pop()
  print(students_in_poetry[index])
  index += 1
"""

#Their way (to print it in list [] form)
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)