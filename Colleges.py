import tkinter as tk
from tkinter import *
import csv


root = tk.Tk()
root.title("Colleges")
root.geometry("300x300")
global top
top = tk.Frame(root)
top.grid()
global bottom
bottom = tk.Frame(root)
bottom.grid()


def hide_bottom():
    root.geometry("300x300")
    for widget in bottom.winfo_children():
        widget.destroy()


class College:
    def __init__(self, cId, cName, course, city, fees, pin):
        self.collegeId = cId
        self.collegeName = cName
        self.courseType = course
        self.city = city
        self.fees = fees
        self.pinCode = pin

    def register(self):
        with open('colleges.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([self.collegeId, self.collegeName, self.courseType, self.city, self.fees, self.pinCode])
        l1 = Label(bottom, text="Successfully registered college!")
        l1.grid(columnspan=3, row=8)


def newCollege(cId, cName, course, city, fees, pin):
    obj = College(cId, cName, course, city, fees, pin)
    obj.register()


def register():
    hide_bottom()
    l1 = Label(bottom, text="College Id: ")
    l1.grid(column=0, row=1)
    cId = Entry(bottom, width=30)
    cId.grid(column=1, row=1, columnspan=2)
    l2 = Label(bottom, text="College Name: ")
    l2.grid(column=0, row=2)
    cName = Entry(bottom, width=30)
    cName.grid(column=1, row=2, columnspan=2)
    l3 = Label(bottom, text="Course: ")
    l3.grid(column=0, row=3)
    course = Entry(bottom, width=30)
    course.grid(column=1, row=3, columnspan=2)
    l4 = Label(bottom, text="City: ")
    l4.grid(column=0, row=4)
    city = Entry(bottom, width=30)
    city.grid(column=1, row=4, columnspan=2)
    l5 = Label(bottom, text="Fees: ")
    l5.grid(column=0, row=5)
    fees = Entry(bottom, width=30)
    fees.grid(column=1, row=5, columnspan=2)
    l6 = Label(bottom, text="Pincode: ")
    l6.grid(column=0, row=6)
    pin = Entry(bottom, width=30)
    pin.grid(column=1, row=6, columnspan=2)
    btn = Button(bottom, text="Submit", command=lambda: newCollege(cId.get(), cName.get(), course.get(), city.get(), fees.get(), pin.get()))
    btn.grid(columnspan=3, row=7)


def searchCollege(cName, course):
    l1 = Label(bottom)
    l1.grid(columnspan=3, row=4)
    success = True
    with open('colleges.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            if cName in i and course in i:
                if success:
                    l1.configure(text="Colleges Found!")
                    success = False
                root.geometry("525x300")
                str1 = "College Id= "+i[0]+", College Name= "+i[1]+", Course= "+i[2]+", City= "+i[3]+", Fees= "+i[4]+", Pincode= "+i[5]
                l2 = Label(bottom, text=str1).grid(columnspan=3)
    if success:
        l1.configure(text="No Colleges found for the given name and course")


def search():
    hide_bottom()
    l1 = Label(bottom, text="College Name: ")
    l1.grid(column=0, row=1, sticky="e")
    cName = Entry(bottom, width=25)
    cName.grid(column=1, row=1, columnspan=2, sticky="w")
    l2 = Label(bottom, text="Course: ")
    l2.grid(column=0, row=2, sticky="e")
    course = Entry(bottom, width=25)
    course.grid(column=1, row=2, columnspan=2, sticky="w")
    btn = Button(bottom, text="Submit", command=lambda: searchCollege(cName.get(), course.get()))
    btn.grid(columnspan=3, row=3)


def removeCollege(cId):
    li = list()
    with open('colleges.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            li.append(i)
    with open('colleges.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for lines in li:
            if lines[0] == str(cId):
                continue
            else:
                csv_writer.writerow(lines)
    str1 = "College with Id: " + str(cId) + " removed successfully!"
    l1 = Label(bottom, text=str1)
    l1.grid(columnspan=3, row=3)


def remove():
    hide_bottom()
    l1 = Label(bottom, text="College Id: ")
    l1.grid(column=0, row=1)
    cId = Entry(bottom, width=30)
    cId.grid(column=1, row=1, columnspan=2)
    btn = Button(bottom, text="Submit", command=lambda: removeCollege(cId.get()))
    btn.grid(columnspan=3, row=2)


bt1 = Button(top, text="Register College", command=register)
bt1.grid(column=0, row=0)
bt2 = Button(top, text="Search Colleges", command=search)
bt2.grid(column=1, row=0)
bt3 = Button(top, text="Remove College", command=remove)
bt3.grid(column=2, row=0)
root.mainloop()