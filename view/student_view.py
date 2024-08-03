from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.student import Student
from controller.student_controller import StudentController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk


class StudentView:

    def save_student2(self):
        name = self.name.get_variable()
        family = self.family.get_variable()
        father_name = self.father_name.get_variable()
        national_id = self.natinal_id.get_variable()
        degree = self.degree.get_variable()
        major = self.major.get_variable()
        grade = self.grade.get_variable()
        phone_number = self.phone_number.get_variable()
        email_address = self.email_address.get_variable()

        status, student = StudentController.save(name, family, father_name, national_id, degree, major, grade,
                                                 phone_number, email_address)
        if status:
            msg.showinfo("info", "the student was successfully registered")
        else:
            msg.showerror("showerror", student)

    def save_student(self):
        self.master = Tk()
        self.master.geometry("800x800")

        self.name = TextWithLabel(self.master, "student name", 10, 60)
        self.family = TextWithLabel(self.master, "student family", 10, 90)
        self.father_name = TextWithLabel(self.master, "father name", 10, 120)
        self.natinal_id = TextWithLabel(self.master, "national id", 10, 150)
        self.degree = TextWithLabel(self.master, "degree", 10, 180)
        self.major = TextWithLabel(self.master, "major", 10, 210)
        self.grade = TextWithLabel(self.master, "grade", 10, 240)
        self.phone_number = TextWithLabel(self.master, "phone", x=10, y=270)
        self.email_address = TextWithLabel(self.master, "email address", 10, 300)

        Button(self.master, text="save", command=self.save_student2).place(x=10, y=350)
        self.master.mainloop()

    def edit_student(self):
        self.master = Tk()
        self.master.geometry("600x400")
        self.std_id = TextWithLabel(self.master, "search student", 10, 20)
        Button(self.master, text="search", command=self.search).place(x=10, y=40)
        self.master.mainloop()

    def edit_student2(self):
        id = self.std_id.get_variable()
        name = self.name.get_variable()
        family = self.family.get_variable()
        father_name = self.father_name.get_variable()
        national_id = self.natinal_id.get_variable()
        degree = self.degree.get_variable()
        major = self.major.get_variable()
        grade = self.grade.get_variable()
        phone_number = self.phone_number.get_variable()
        email_address = self.email_address.get_variable()
        status, student = StudentController.save(name, family, father_name, national_id, degree, major, grade,
                                                 phone_number, email_address)
        if status:
            msg.showinfo("info", "the student was successfully edited")
        else:
            msg.showerror("showerror", student)

    def search(self):
        id = self.std_id.get_variable()
        id = int(id)
        status, student = StudentController.find_by_id(id)
        if status:
            print(student)
            self.name = TextWithLabel(self.master, "student name", 10, 70)
            self.name.set_variable(student.name)
            self.family = TextWithLabel(self.master, "student family", 10, 100)
            self.family.set_variable(student.family)
            self.father_name = TextWithLabel(self.master, "father name", 10, 130)
            self.father_name.set_variable(student.father_name)
            self.natinal_id = TextWithLabel(self.master, "national id", 10, 160)
            self.natinal_id.set_variable(student.national_id)
            self.degree = TextWithLabel(self.master, "degree", 10, 190)
            self.degree.set_variable(student.degree)
            self.major = TextWithLabel(self.master, "major", 10, 220)
            self.major.set_variable(student.major)
            self.grade = TextWithLabel(self.master, "grade", 10, 250)
            self.grade.set_variable(student.grade)
            self.phone_number = TextWithLabel(self.master, "phone", x=10, y=280)
            self.phone_number.set_variable(student.phone_number)
            self.email_address = TextWithLabel(self.master, "email address", 10, 310)
            self.email_address.set_variable(student.email_address)
            Button(self.master, text="edit", command=self.edit_student2).place(x=10, y=350)
    def student_table_click(self, row):
        print(row)
    def detaile_student(self):
        self.win = Tk()
        self.win.title("Student View")
        self.win.geometry("1000x800")

        student_table = Table(self.win,
                                ["id","name", "family", "father name", "national id", "degree",
                                 "major", "grade","phone number","email address","deleted"],
                                [60, 80, 80, 80, 150, 80, 80, 60,150,150], 20, 20,
                                self.student_table_click)

        self.win.mainloop()
