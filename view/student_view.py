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
        self.master.title("Storing Student Info")
        self.master.geometry("600x600")

        self.name = TextWithLabel(self.master, "student name" ,10, 50,distance=100)
        self.family = TextWithLabel(self.master, "student family", 10, 100,distance=100)
        self.father_name = TextWithLabel(self.master, "father name", 10, 150,distance=100)
        self.natinal_id = TextWithLabel(self.master, "national id", 10, 200,distance=100)
        self.degree = TextWithLabel(self.master, "degree", 10, 250,distance=100)
        self.major = TextWithLabel(self.master, "major", 10, 300,distance=100)
        self.grade = TextWithLabel(self.master, "grade", 10, 350,distance=100)
        self.phone_number = TextWithLabel(self.master, "phone", x=10, y=400,distance=100)
        self.email_address = TextWithLabel(self.master, "email address", 10, 450,distance=100)

        Button(self.master, text="save",width=15,bg="blue",font=("Arial",16) ,command=self.save_student2).place(x=200, y=550)
        self.master.mainloop()

    def edit_student(self):
        self.master = Tk()
        self.master.title("Edit Student Info")
        self.master.geometry("500x500")
        self.std_id = TextWithLabel(self.master, "search student", 10, 20, distance=100)
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
        self.master = Tk()
        self.master.title("Students Info Table")
        self.master.geometry("1200x400")

        student_table = Table(self.master,
                              ["id", "name", "family", "father name", "national id", "degree",
                               "major", "grade", "phone number", "email address", "deleted"],
                              [60, 80, 120, 80, 150, 80, 150, 60, 150, 150, 50], 20, 20,
                              self.student_table_click)
        status, data_ = StudentController.find_all()
        data_list = []
        for data in data_:
            print(data)
            data_list.append([data.id, data.name, data.family, data.father_name, data.national_id, data.degree,
                              data.major, data.grade, data.phone_number, data.email_address, data.deleted])
        print(data_list)
        student_table.refresh_table(data_list)
        self.master.mainloop()
