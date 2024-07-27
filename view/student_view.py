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
        self.win.geometry("500x500")

        student_table = Table(self.win,
                              ["id", "name", "family", "father_name", "national_id", "degree", "major", "grade",
                               "phone_number", "email_address", "deleted"],
                              [60, 80, 80, 80, 60, 60, 60, 60, 80, 80, 50], 20, 20,
                              self.student_table_click)
        Button(self.win,text  = "اضافه کردن دانشجو",command=self.save_student).place(x=300,y=300)
        #self.student_table.refresh_table(self.student_da.find_all())

        self.win.mainloop()

    def save_student(self):
        print("hiiiii")