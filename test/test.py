from controller.student_controller import *
# from controller.professor_controller import *
from controller.course_controller import *
#from controller.professor_controller import ProfessorController
from controller.select_course_controller import *
from model.entity import *
from model.entity.professor import Professor
from datetime import datetime
# from model.entity.professor import Professor
# from model.entity.course import Course


# student = Student("roya","mirhosseini","amir","0018453139","bachelor","electrical engineering","17","09128404487","royamirhoseini95@gmail.com")
# student_da =  DataAccess(Student)
# student.id = 2
# print(student)


# course = Course("56749","electronic 2","theoretical",3,"electronic 1","english","in person","2024/09/09","2025/03/05",professor)
# print(course)


# StudentController.save("roya","mirhosseini","amir","0018453139","bachelor","electrical engineering","17","09128404487","royamirhoseini95@gmail.com")
#status,professor = ProfessorController.save("meysam","basiri","electrical and computer","electronic","official employment","meysam.basiri@iau.ac.ir")
#professor = Professor("meysam","basiri","engineering","electrical","contractual employment","meysam.basiri@iau.ac.ir")

#CourseController.save("4567", "digital systems 2", "theoretical", "3", "digital systems 1", "english", "in person",
#                      "2024-07-07", "2024-07-07", 1)
status,student = StudentController.save("sara","jelveh","ahmad","0098783545","bachelor","art","14","09123459876","gfgf@gmail.com")
status,course = CourseController.save("5678","mathmatic","theoretical","1","physics","english","in person","2024-03-03","2025-04-04","1")
status , weijewui = SelectCourseController.save(1,1,"2024-2-3")
print(status,weijewui)
