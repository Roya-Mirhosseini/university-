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
        self.win = Tk()
        self.win.title("Course View")
        self.win.geometry("1000x800")

        course_table = Table(self.win,
                             ["id", "code", "course_name", "course_type", "unit_number", "prerequisite",
                              "language", "hold_type", "start_date", "end_date", "professor_id", "deleted"],
                             [60, 60, 80, 80, 60, 170, 80, 80, 120, 120, 60, 50], 20, 20,
                             self.course_table_click)
        Button(self.win, text="اضافه کردن درس ", command=self.save_course).place(x=100, y=300)
        Button(self.win, text="ویرایش اطلاعات درس", command=self.edit_course).place(x=250, y=300)
        Button(self.win, text="نمایش اطلاعات کامل درس", command=self.detaile_course).place(x=400, y=300)
        # self.student_table.refresh_table(self.student_da.find_all())

        self.win.mainloop()

    def save_course2(self):
        id = self.id.text_box.get()
        code = self.code.text_box.get()
        course_name = self.course_name.text_box.get()
        course_type = self.course_type.text_box.get()
        unit_number = self.unit_number.text_box.get()
        prerequisite = self.prerequisite.text_box.get()
        language = self.language.text_box.get()
        hold_type = self.hold_type.text_box.get()
        start_date = self.start_date.text_box.get()
        end_date = self.end_date.text_box.get()
        professor_id = self.professor_id.text_box.get()

        status, course = CourseController.save(code, course_name, course_type, unit_number, prerequisite, language,
                                               hold_type, start_date, end_date, professor_id)
        if status:
            msg.showinfo("info", "the course was successfully created")
        else:
            msg.showerror("showerror", course)

    def save_course(self):
        self.master = Tk()
        self.master.geometry("400x400")
        self.id = TextWithLabel(self.master, "course id", 10, 30)
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
        pass

    def detaile_course(self):
        pass
