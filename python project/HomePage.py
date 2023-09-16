from tkinter import *
from login import LoginForm
import login
from login import isLogin
home = Tk()
home.geometry("500x350")
home.configure(bg="white")
home.title("Home Page")
home.resizable(False, False)

if isLogin == False:
    home.destroy()
else:
    pass


def PatientPage():
    import PatientPage


def doctorsPage():
    import doctor


def logout():
    login.isLogin = False
    home.destroy()
    LoginForm.destroy()


title = Label(home, text="Dental Clinic 🦷", font=(
    "Helvetica", 30), bg="wheat").pack()

Patient = Button(home, text="PatientPage", width=25, height=5, bg="#40a944", activebackground="lightgreen", command=PatientPage).place(
    relx=0.2, rely=0.5, anchor=CENTER)
viewRecords = Button(home, width=25, height=5, text="Doctors", bg="yellow", activebackground="orange", command=doctorsPage).place(
    relx=0.8, rely=0.5, anchor=CENTER)
Logout = Button(home, text="Logout", width=25, command=logout).place(
    relx=1, rely=1, anchor="se")


home.mainloop()
