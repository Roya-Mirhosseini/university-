from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.course import Course
from controller.course_controller import CourseController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk


class CourseView:
    def course_table_click(self, row):
        print(row)

    def __init__(self):
        self.Course_da = DataAccess(Course)
        # self.win = Tk()
        # self.win.title("Course View")
        # self.win.geometry("1000x800")
        #
        # course_table = Table(self.win,
        #                      ["id", "code", "course_name", "course_type", "unit_number", "prerequisite",
        #                       "language", "hold_type", "start_date", "end_date", "professor_id", "deleted"],
        #                      [60, 60, 80, 80, 60, 170, 80, 80, 120, 120, 60, 50], 20, 20,
        #                      self.course_table_click)
        # Button(self.win, text="اضافه کردن درس ", command=self.save_course).place(x=100, y=300)
        # Button(self.win, text="ویرایش اطلاعات درس", command=self.edit_course).place(x=250, y=300)
        # Button(self.win, text="نمایش اطلاعات کامل درس", command=self.detaile_course).place(x=400, y=300)
        # self.student_table.refresh_table(self.student_da.find_all())

        # self.win.mainloop()

    def save_course2(self):
        code = self.code.get_variable()
        course_name = self.course_name.get_variable()
        course_type = self.course_type.get_variable()
        unit_number = self.unit_number.get_variable()
        prerequisite = self.prerequisite.get_variable()
        language = self.language.get_variable()
        hold_type = self.hold_type.get_variable()
        start_date = self.start_date.get_variable()
        end_date = self.end_date.get_variable()
        professor_id = self.professor_id.get_variable()

        status, course = CourseController.save(code, course_name, course_type, unit_number, prerequisite, language,
                                               hold_type, start_date, end_date, professor_id)
        if status:
            msg.showinfo("info", "the course was successfully created")
        else:
            msg.showerror("showerror", course)

    def save_course(self):
        self.master = Tk()
        self.master.geometry("400x400")
        # self.id = TextWithLabel(self.master, "course id", 10, 30)
        self.code = TextWithLabel(self.master, "code", 10, 60)
        self.course_name = TextWithLabel(self.master, "course name", 10, 90)
        self.course_type = TextWithLabel(self.master, "course type", 10, 120)
        self.unit_number = TextWithLabel(self.master, "unit number", 10, 150)
        self.prerequisite = TextWithLabel(self.master, "prerequisite", 10, 180)
        self.language = TextWithLabel(self.master, "language", 10, 210)
        self.hold_type = TextWithLabel(self.master, "hold type", 10, 240)
        self.start_date = TextWithLabel(self.master, "start date", 10, 270)
        self.end_date = TextWithLabel(self.master, "end date", 10, 300)
        self.professor_id = TextWithLabel(self.master, "professor id", 10, 330)

        Button(self.master, text="save", command=self.save_course2).place(x=10, y=350)
        self.master.mainloop()

    def edit_course(self):
        self.master = Tk()
        self.master.geometry("500x500")
        self.course_id = TextWithLabel(self.master, "search course", 10, 20)
        Button(self.master, text="search", command=self.search).place(x=10, y=40)
        self.master.mainloop()

    def edit_course2(self):
        id = self.course_id.get_variable()
        code = self.code.get_variable()
        course_name = self.course_name.get_variable()
        course_type = self.course_type.get_variable()
        unit_number = self.unit_number.get_variable()
        prerequisite = self.prerequisite.get_variable()
        language = self.language.get_variable()
        hold_type = self.hold_type.get_variable()
        start_date = self.start_date.get_variable()
        end_date = self.end_date.get_variable()
        professor_id = self.professor_id.get_variable()
        status, course = CourseController.save(code, course_name, course_type, unit_number, prerequisite, language,
                                               hold_type, start_date, end_date, professor_id)
        if status:
            msg.showinfo("info", "the course was successfully edited")
        else:
            msg.showerror("showerror", course)

    def search(self):
        id = self.course_id.get_variable()
        id = int(id)
        status, course = CourseController.find_by_id(id)
        if status:
            print(course)
            self.code = TextWithLabel(self.master, "code", 10, 70)
            self.code.set_variable(course.code)
            self.course_name = TextWithLabel(self.master, "course name", 10, 100)
            self.course_name.set_variable(course.course_name)
            self.course_type = TextWithLabel(self.master, "course type", 10, 130)
            self.course_type.set_variable(course.course_type)
            self.unit_number = TextWithLabel(self.master, "unit number", 10, 160)
            self.unit_number.set_variable(course.unit_number)
            self.prerequisite = TextWithLabel(self.master, "prerequisite", 10, 190)
            self.prerequisite.set_variable(course.prerequisite)
            self.language = TextWithLabel(self.master, "language", 10, 220)
            self.language.set_variable(course.language)
            self.hold_type = TextWithLabel(self.master, "hold_type", 10, 250)
            self.hold_type.set_variable(course.hold_type)
            self.start_date = TextWithLabel(self.master, "start date", x=10, y=280)
            self.start_date.set_variable(course.start_date)
            self.end_date = TextWithLabel(self.master, "end date", 10, 310)
            self.end_date.set_variable(course.end_date)
            self.professor_id = TextWithLabel(self.master, "professor id", 10, 310)
            self.professor_id.set_variable(course.professor_id)

            Button(self.master, text="edit", command=self.edit_course2).place(x=10, y=350)

    def detaile_course(self):
        self.master = Tk()
        self.master.title("Course View")
        self.master.geometry("1200x400")

        course_table = Table(self.master,
                                ["id", "code", "course name", "course type", "unit number", "prerequisite",
                                 "language", "hold type","start date","end date","professor id","deleted"],
                                [60, 80, 120, 80, 100, 150, 80,100,100,100,60, 50], 20, 20,
                                self.course_table_click)
        status, data_ = CourseController.find_all()
        data_list = []
        for data in data_:
            print(data)
            data_list.append(
                [data.id, data.code, data.course_name, data.course_type, data.unit_number, data.prerequisite,
                 data.language,data.hold_type,data.start_date,data.end_date,data.professor_id, data.deleted])
        print(data_list)
        course_table.refresh_table(data_list)
        self.master.mainloop()


