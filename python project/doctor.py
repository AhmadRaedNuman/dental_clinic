from tkinter import *
from connect import cursor, DentalClinic
from tkinter import messagebox
import pandas as ps

doctor = Tk()
doctor.geometry("800x500")
doctor.title('Doctors Page')
doctor.resizable(False, False)
# --------------------------------------------------------


def backButton():
    doctor.withdraw()


def add_doctor():
    name = Dr_name.get()
    phone = phoneNo.get()
    Spec = spec.get()
    if len(name) < 5:
        messagebox.showwarning(message="Add Name at least 5 char")
    if len(phone) != 10:
        messagebox.showwarning(message="must be 10 numbers")
    sql = "INSERT INTO doctor (DoctorName,DoctorPhone,specialtyDr) VALUES (%s,%s,%s)"
    value = (name, phone, Spec)
    try:
        cursor.execute(sql, value)
        DentalClinic.commit()
        messagebox.showinfo(title="Record Added",
                            message="record has been successfully added.")
    except Exception as e:
        messagebox.showerror(title="DataBase Error",
                             message="please add the records to the database.")
        print(e)
    doctor.update()


def selectDoctor():
    sql = "SELECT DoctorName from doctor"
    cursor.execute(sql)
    result = cursor.fetchall()
    result_list = [row[0] for row in result]
    return result_list


def deleteDoc():
    name = doc.get()
    sql = "DELETE FROM doctor WHERE DoctorName = %s"
    value = (name,)
    try:
        cursor.execute(sql, value)
        DentalClinic.commit()
        messagebox.showinfo(title='Delete', message="Deleted!")
    except Exception as e:
        messagebox.showwarning(message="Something went wrong")
        print(e)


# =========================================


def selectSpec():
    sql = "SELECT specialtyName FROM specialtydr"
    cursor.execute(sql)
    result = cursor.fetchall()
    result_list = [row[0] for row in result]
    return result_list

# =========================================


def write_to_excel():
    cursor.execute("select * from doctor")
    rows = cursor.fetchall()
    data = ps.DataFrame(rows, columns=[
                        "DoctorID", "DoctorName ", "DoctorPhone", "specialtyDr", ])
    data.to_excel("./execl file/Doctors.xlsx", index=False)
    messagebox.showinfo(title="success", message="Data Exported to excel file")
    print("Data Exported to excel file")

# =========================================


# add doctor form
# name
nameLabel = Label(doctor, text="Doctor Name: ")
nameLabel.place(relx=0.1, rely=0.01)
Dr_name = Entry(doctor)
Dr_name.place(relx=0.2, rely=0.01)

# phone
PhoneLabel = Label(doctor, text="Phone Number: ")
PhoneLabel.place(relx=0.4, rely=0.01)
phoneNo = Entry(doctor)
phoneNo.place(relx=0.52, rely=0.01)

# speciality
spec = StringVar()
specList = selectSpec()
specialty_label = Label(doctor, text="Specialty: ")
specialty_label.place(relx=0.69, rely=0.01)
Spclty = OptionMenu(doctor, spec, *specList)
Spclty.place(relx=0.78, rely=0.01)

# add btn
addbtn = Button(doctor, text="(+) Add Doctor (+)", command=add_doctor,
                width=15, height=2, bg="green", activebackground="#40a944", activeforeground="white", fg="white")
addbtn.place(relx=0.5, rely=0.15, anchor="center")
# ============================================

# delete doctor
selectDoc = selectDoctor()
doc = StringVar()
# default value of the option menu is blank string
doc.set("Select Doctor Name")

deleteSelector = OptionMenu(doctor, doc, *selectDoc)
deleteSelector.place(relx=0.5, rely=0.35, anchor="center")

delete_doctor = Button(doctor, text="(-) Delete Doctor (-)", bg="red", command=deleteDoc,
                       fg="white", activebackground="#d82532", activeforeground="white")
delete_doctor.place(relx=0.5, rely=0.46, anchor="center")
# ==============================================

# view all doctors
viewAllBtn = Button(doctor, text="View All Doctors", width=25, bg='green', fg='#fff', command=write_to_excel,
                    activebackground='#1a964c', activeforeground='#fff').place(relx=0, rely=1, anchor="sw")
# ====================================================================================
# back btn
backBtn = Button(doctor, text="Back", width=25,
                 command=backButton, bg="red", fg="white", activebackground="#d6252e", activeforeground="white")
backBtn.place(
    relx=1, rely=1, anchor="se")

doctor.mainloop()
