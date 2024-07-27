from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.student import Student
from controller.student_controller import StudentController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk


class StudentView:
    def student_table_click(self, row):
        print(row)

    # _________________________________________________________checked up here

    def __init__(self):
        self.Student_da = DataAccess(Student)
        self.win = Tk()
        self.win.title("Student View")
        self.win.geometry("1000x800")

        student_table = Table(self.win,
                              ["id", "name", "family", "father_name", "national_id", "degree", "major", "grade",
                               "phone_number", "email_address", "deleted"],
                              [60, 80, 80, 80, 100, 60, 60, 60, 120, 120, 50], 20, 20,
                              self.student_table_click)
        Button(self.win,text  = "اضافه کردن دانشجو",command=self.save_student).place(x=100,y=300)
        Button(self.win,text  = "ویرایش اطلاعات دانشجو",command=self.edit_student).place(x=250,y=300)
        Button(self.win,text  = "نمایش اطلاعات کامل دانشجو",command=self.detaile_student).place(x=400,y=300)
        #self.student_table.refresh_table(self.student_da.find_all())

        self.win.mainloop()

    def save_student2(self):
        grade = self.grade.text_box.get()
        name = self.name.text_box.get()
        print(name)
        StudentController.save(name, "mirhosseini", "amir", "0018453139", "bachelor", "electrical engineering", grade,
                               "09128404487", "royamirhoseini95@gmail.com")
        print(grade)
    def save_student(self):
        self.master = Tk()
        self.master.geometry("400x400")
        self.id = TextWithLabel(self.master,"student id",10,30)
        self.name = TextWithLabel(self.master,"student name",10,60)
        self.family = TextWithLabel(self.master,"student family",10,90)
        self.father_name = TextWithLabel(self.master,"father name",10,120)
        self.natinal_id = TextWithLabel(self.master,"national id",10,150)
        self.degree = TextWithLabel(self.master,"degree",10,180)
        self.major = TextWithLabel(self.master,"major",10,210)
        self.grade = TextWithLabel(self.master,"grade",10,240)
        self.phone_number = TextWithLabel(self.master,"phone",x=10,y=270)
        self.email_address = TextWithLabel(self.master,"email address",10,300)
        Button(self.master,text="save",command=self.save_student2).place(x=10,y=350)
        self.master.mainloop()


    def edit_student(self):

        print("hello")

    def detaile_student(self):
        print("how are you")