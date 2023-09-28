class Student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list,key =lambda Student: Student.cgpa,reverse=True)
  return sorted_students

students = [
  Student("hari","A123",7.0),
 Student("srikanth","A124",8.9),
  Student("saumya","A125",8.0),
  Student("mahidhar","A126",9.9)
]

sorted_students= sort_students(students)
for student in sorted_students:
 print("Name:{},Roll_Number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))