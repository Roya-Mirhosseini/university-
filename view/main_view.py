from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.course import Course
from controller.course_controller import CourseController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from view.student_view import StudentView
from view.professor_view import ProfessorView
from view.course_view import CourseView
from view.select_course_view import SelectCourseView
from tkinter import StringVar, Label, Entry


class MainView:

    def __init__(self):
        self.win = Tk()
        self.win.title("Main View")
        self.win.geometry("650x900")

        Label(self.win, text="مشخصات دانشجو", width=15, height=1, bg="aqua", font=("Arial", 18)).place(x=215, y=50)

        Button(self.win, text="اضافه کردن", width=15, height=3, bg="aqua", command=self.save_student).place(x=100,
                                                                                                            y=100)
        Button(self.win, text="ویرایش اطلاعات", width=15, height=3, bg="aqua", command=self.edit_student).place(x=250,
                                                                                                                y=100)
        Button(self.win, text="نمایش کامل اطلاعات", width=15, height=3, bg="aqua", command=self.detaile_student).place(
            x=400, y=100)

        Label(self.win, text="مشخصات استاد", width=15, height=1, bg="light blue", font=("Arial", 18)).place(x=215,
                                                                                                            y=200)
        Button(self.win, text="اضافه کردن ", width=15, height=3, bg="light blue", command=self.save_professor).place(
            x=100, y=250)
        Button(self.win, text="ویرایش اطلاعات", width=15, height=3, bg="light blue", command=self.edit_professor).place(
            x=250, y=250)
        Button(self.win, text="نمایش کامل اطلاعات", width=15, height=3, bg="light blue",
               command=self.detaile_professor).place(x=400, y=250)

        Label(self.win, text="مشخصات درس", width=15, height=1, bg="pink", font=("Arial", 18)).place(x=215, y=350)

        Button(self.win, text="اضافه کردن ", width=15, height=3, bg="pink", command=self.save_course).place(x=100,
                                                                                                            y=400)
        Button(self.win, text="ویرایش اطلاعات", width=15, height=3, bg="pink", command=self.edit_course).place(x=250,
                                                                                                               y=400)
        Button(self.win, text="نمایش کامل اطلاعات", width=15, height=3, bg="pink", command=self.detaile_course).place(
            x=400, y=400)

        Button(self.win, text="انتخاب واحد", width=15, height=3, bg="teal", command=self.save_select_course).place(
            x=250, y=550)
        self.win.mainloop()

    def save_student(self):
        save = StudentView()
        save.save_student()

    def edit_student(self):
        edit = StudentView()
        edit.edit_student()

    def detaile_student(self):
        detaile = StudentView()
        detaile.detaile_student()

    def save_professor(self):
        save = ProfessorView()
        save.save_professor()

    def edit_professor(self):
        edit = ProfessorView()
        edit.edit_professor()

    def detaile_professor(self):
        detaile = ProfessorView()
        detaile.detaile_professor()

    def save_course(self):
        save = CourseView()
        save.save_course()

    def edit_course(self):
        edit = CourseView()
        edit.edit_course()

    def detaile_course(self):
        detaile = CourseView()
        detaile.detaile_course()

    def save_select_course(self):
        save = SelectCourseView()
        save.save_select_course()
