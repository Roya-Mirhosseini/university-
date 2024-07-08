from datetime import date, datetime

from mft.model.entity.professor import Professor
#
# from mft.model.entity.student import Student
from mft.model.tools.validator import *
# student = Student("roya","mirhosseini","amir","0018453139","master","electrical engineering","17","09128404487","royamirhoseini95@gmail.com")
# print(student)


from mft.model.entity.course import Course
professor = Professor("ali","aat","engineering","electrical","contractual employment","jhdjdh@iau.ac,")
course = Course("56749","electronic 2","theoretical",3,"electronic 1","english","in person","2024/09/09","2025/03/05",professor)

print(course)