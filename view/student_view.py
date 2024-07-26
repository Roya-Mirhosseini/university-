from model.da.da import DataAccess
from view.component.label_text import TextWithLabel
from view.component.table import Table
from model.entity.student import Student
from controller.student_controller import StudentController
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

class StudentView:
    def student_table_click(self,row):
        print (row)
#_________________________________________________________checked up here


    def __init__(self):
        self.Person_da = DataAccess(Person)
        self.medical_report_da = DataAccess(MedicalReport)
        self.win = Tk()
        self.title("Person MedicalReport View")
        self.win.geometry("500x500")

        person_table = Table(self.win,
                             ["Id", "Name", "Family", "NationalId", "Status"],
                             [60,80,80,80,50], 20, 20 ,
                             self.person_table_click)

        self.person_table.refresh_table(self.person_da.find_all())



        medical_report_table = Table(self.win,
                             ["Id","Disease","ReportGroup","DateTime", "Deleted"],
                             [60,80,80,80,60],300,20 ,
                             self.medical_report_table_click)

        self.win.mainloop()