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
        # self.win = Tk()
        # self.win.title("Professor View")
        # self.win.geometry("1000x800")
        #
        # professor_table = Table(self.win,
        #                         ["id", "name", "family", "faculty", "academic_department", "employment_status",
        #                          "academic_email", "deleted"],
        #                         [60, 80, 80, 120, 150, 150, 120, 50], 20, 20,
        #                         self.professor_table_click)
        # # Button(self.win, text="اضافه کردن استاد ", command=self.save_professor).place(x=100, y=300)
        # # Button(self.win, text="ویرایش اطلاعات استاد", command=self.edit_professor).place(x=250, y=300)
        # # Button(self.win, text="نمایش اطلاعات کامل استاد", command=self.detaile_professor).place(x=400, y=300)
        # # self.student_table.refresh_table(self.student_da.find_all())
        #
        # self.win.mainloop()

    def save_professor2(self):
        name = self.name.get_variable()
        family = self.family.get_variable()
        faculty = self.faculty.get_variable()
        academic_department = self.academic_department.get_variable()
        employment_status = self.employment_status.get_variable()
        academic_email = self.academic_email.get_variable()

        status, professor = ProfessorController.save(name, family, faculty, academic_department, employment_status,
                                                     academic_email)
        if status:
            msg.showinfo("info", "the professor was successfully recruited")
        else:
            msg.showerror("showerror", professor)

    def save_professor(self):
        self.master = Tk()
        self.master.title("Storing Professor Info")
        self.master.geometry("600x600")

        self.name = TextWithLabel(self.master, "professor name", 10, 50,distance=120)
        self.family = TextWithLabel(self.master, "professor family", 10, 100,distance=120)
        self.faculty = TextWithLabel(self.master, "faculty", 10, 150,distance=120)
        self.academic_department = TextWithLabel(self.master, "academic department", 10, 200,distance=120)
        self.employment_status = TextWithLabel(self.master, "employment status", 10, 250,distance=120)
        self.academic_email = TextWithLabel(self.master, "academic email", 10, 300,distance=120)

        Button(self.master, text="save",width=15,bg="blue",font=("Arial",16), command=self.save_professor2).place(x=200, y=400)
        self.master.mainloop()

    def edit_professor(self):
        self.master = Tk()
        self.master.title("Edit Professor Info")
        self.master.geometry("600x600")
        self.professor_id = TextWithLabel(self.master, "search professor", 10, 50,distance=120)
        Button(self.master, text="search",width=15,bg="blue",font=("Arial",14), command=self.search).place(x=200, y=400)
        self.master.mainloop()

    def edit_professor2(self):
        id = self.professor_id.get_variable()
        name = self.name.get_variable()
        family = self.family.get_variable()
        faculty = self.faculty.get_variable()
        academic_department = self.academic_department.get_variable()
        employment_status = self.employment_status.get_variable()
        academic_email = self.academic_email.get_variable()
        status, professor = ProfessorController.save(name, family, faculty, academic_department, employment_status,
                                                     academic_email)
        if status:
            msg.showinfo("info", "the professor was successfully edited")
        else:
            msg.showerror("showerror", professor)

    def search(self):
        id = self.professor_id.get_variable()
        id = int(id)
        status, professor = ProfessorController.find_by_id(id)
        if status:
            print(professor)
            self.name = TextWithLabel(self.master, "professor name", 10, 100,distance=120)
            self.name.set_variable(professor.name)
            self.family = TextWithLabel(self.master, "professor family", 10, 150,distance=120)
            self.family.set_variable(professor.family)
            self.faculty = TextWithLabel(self.master, "faculty", 10, 200,distance=120)
            self.faculty.set_variable(professor.faculty)
            self.academic_department = TextWithLabel(self.master, "academic department", 10, 250,distance=120)
            self.academic_department.set_variable(professor.academic_department)
            self.employment_status = TextWithLabel(self.master, "employment status", 10, 300,distance=120)
            self.employment_status.set_variable(professor.employment_status)
            self.academic_email = TextWithLabel(self.master, "academic email", 10, 350,distance=120)
            self.academic_email.set_variable(professor.academic_email)

            Button(self.master, text="edit",width=15,bg="blue",font=("Arial",14), command=self.edit_professor2).place(x=10, y=400)

    def detaile_professor(self):
        self.master = Tk()
        self.master.title("Professors Info Table")
        self.master.geometry("1000x400")

        professor_table = Table(self.master,
                              ["id", "name", "family", "faculty", "academic department", "employment status",
                               "academic email", "deleted"],
                              [60, 80, 80, 150, 150, 150, 150, 50], 20, 20,
                              self.professor_table_click)
        status, data_ = ProfessorController.find_all()
        data_list = []
        for data in data_:
            print(data)
            data_list.append([data.id, data.name, data.family, data.faculty, data.academic_department, data.employment_status,
                              data.academic_email, data.deleted])
        print(data_list)
        professor_table.refresh_table(data_list)
        self.master.mainloop()

