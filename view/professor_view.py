from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.professor import Professor
from controller.professor_controller import ProfessorController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk


class ProfessorView:
    def professor_table_click(self, row):
        print(row)

    def __init__(self):
        self.Professor_da = DataAccess(Professor)
        self.win = Tk()
        self.win.title("Professor View")
        self.win.geometry("1000x800")

        professor_table = Table(self.win,
                                ["id", "name", "family", "faculty", "academic_department", "employment_status",
                                 "academic_email", "deleted"],
                                [60, 80, 80, 120, 150, 150, 120, 50], 20, 20,
                                self.professor_table_click)
        Button(self.win, text="اضافه کردن استاد ", command=self.save_professor).place(x=100, y=300)
        Button(self.win, text="ویرایش اطلاعات استاد", command=self.edit_professor).place(x=250, y=300)
        Button(self.win, text="نمایش اطلاعات کامل استاد", command=self.detaile_professor).place(x=400, y=300)
        # self.student_table.refresh_table(self.student_da.find_all())

        self.win.mainloop()

    # --------------------------------------------------------------------------------------------------------------cheched up to here
    def save_professor2(self):
        id = self.id.text_box.get()
        name = self.name.text_box.get()
        family = self.family.text_box.get()
        faculty = self.faculty.text_box.get()
        academic_department = self.academic_department.text_box.get()
        employment_status = self.employment_status.text_box.get()
        academic_email = self.academic_email.text_box.get()

        status, professor = ProfessorController.save(name, family, faculty, academic_department, employment_status,
                                                     academic_email)
        if status:
            msg.showinfo("info", "the professor was successfully recruited")
        else:
            msg.showerror("showerror", professor)

    def save_professor(self):
        self.master = Tk()
        self.master.geometry("400x400")
        self.id = TextWithLabel(self.master, "professor id", 10, 30)
        self.name = TextWithLabel(self.master, "professor name", 10, 60)
        self.family = TextWithLabel(self.master, "professor family", 10, 90)
        self.faculty = TextWithLabel(self.master, "faculty", 10, 120)
        self.academic_department = TextWithLabel(self.master, "academic department", 10, 150)
        self.employment_status = TextWithLabel(self.master, "employment status", 10, 180)
        self.academic_email = TextWithLabel(self.master, "academic email", 10, 210)

        Button(self.master, text="save", command=self.save_professor2).place(x=10, y=350)
        self.master.mainloop()

    def edit_professor(self):
        print("hello")

    def detaile_professor(self):
        print("how are you")

