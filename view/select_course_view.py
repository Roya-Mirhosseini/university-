from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.select_course import SelectCourse
from controller.select_course_controller import SelectCourseController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import datetime
now = datetime.datetime.now()


class SelectCourseView:
    # def select_course_table_click(self, row):
    #     print(row)
    #
    # def __init__(self):
    #     self.SelectCourse_da = DataAccess(SelectCourse)
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

    def save_select_course2(self):
        course_id = self.course_id.get_variable()
        course_id = int(course_id)
        student_id = self.student_id.get_variable()
        student_id = int(student_id)
        date_ = datetime.datetime.now()
        status, select_course = SelectCourseController.save(course_id, student_id,date_)
        if status:
            msg.showinfo("info", "the select course was successfully created")
        else:
            msg.showerror("showerror", select_course)

    def save_select_course(self):
        self.master = Tk()
        self.master.title("Select Course")
        self.master.geometry("400x400")

        self.course_id = TextWithLabel(self.master, "course", 10, 50)
        self.student_id = TextWithLabel(self.master, "student", 10, 100)
        #self.date_time = TextWithLabel(self.master, "date time", 10, 120)

        Button(self.master, text="save",width=15,bg="blue",font=("Arial",14), command=self.save_select_course2).place(x=100, y=200)

        self.master.mainloop()


