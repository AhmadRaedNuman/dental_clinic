from tkinter import *
import pandas as ps
from connect import cursor, DentalClinic
from tkinter import messagebox

addPatientPage = Tk()
addPatientPage.geometry("800x500")
addPatientPage.title("Patient Page")


def backButton():
    addPatientPage.withdraw()
# ============================================================


def selectMenu():
    sql = "SELECT TreatmentName FROM treatment"
    cursor.execute(sql)
    result = cursor.fetchall()
    result_list = [row[0] for row in result]
    return result_list

# ==========================================================


def getInfo():
    name = PatientName.get()
    age = PatientAge.get()
    phone = PatientPhone.get()
    smoker = smoke.get()
    treatment = var.get()

    if len(age) > 3 or len(age) == 0:
        messagebox.showwarning(title="Age Entry error", message="Check of Age")
    else:
        pass
    if len(phone) != 10:
        messagebox.showwarning(title="Phone Number error",
                               message="Phone Number must be 10 numbers")
    else:
        pass
    if smoker == '0':
        smoker = 'No'
    else:
        smoker = 'Yes'
    if treatment == None:
        messagebox.showwarning('Warning', 'Please Select a Treatment')
    sql = "INSERT INTO patient (`patientName`, `age`, `patientPhone`, `type of treatment`, `Smoking`) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, phone, treatment, smoker)
    try:
        cursor.execute(sql, values)
        DentalClinic.commit()
        messagebox.showinfo(
            title="Record Added", message="Patient record has been successfully added.")
    except Exception as e:
        messagebox.showerror(
            title="Database Error", message="please add the records to the database.")
        print(e)
# =========================================================================


def write_to_excel():
    cursor.execute("select * from patient")
    rows = cursor.fetchall()
    data = ps.DataFrame(rows, columns=[
                        "PatientID", "patientName", "age", "patientPhone", "type of treatment", "Smoking"])
    data.to_excel("./execl file/patients.xlsx", index=False)
    messagebox.showinfo(title="success", message="Data Exported to excel file")
    print("Data Exported to excel file")


# =========================================================================
title = Label(addPatientPage, text="Dental Clinic 🦷",
              font=("Helvetica", 30), bg="wheat")
title.pack(side=TOP)

# name
PatientnameLabel = Label(addPatientPage, text="Patient name: ")
PatientnameLabel.place(relx=0.1, rely=0.15)
PatientName = Entry(addPatientPage)
PatientName.place(relx=0.2, rely=0.15)

# age
PatientAgeLabel = Label(addPatientPage, text="Patient Age: ")
PatientAgeLabel.place(relx=0.4, rely=0.15)
PatientAge = Entry(addPatientPage)
PatientAge.place(relx=0.5, rely=0.15)

# phone
PatientPhoneLabel = Label(addPatientPage, text="Phone Number: ")
PatientPhoneLabel.place(relx=0.7, rely=0.15)
PatientPhone = Entry(addPatientPage)
PatientPhone.place(relx=0.82, rely=0.15)

# treatment
var = StringVar()
var.set("Select Treatment")
treatment_options = selectMenu()
TreatmentDrop = OptionMenu(
    addPatientPage, var, *treatment_options)
TreatmentDrop.place(relx=0.55, rely=0.25)

# smoke
smoke = StringVar()
SmokerLabel = Label(addPatientPage, text="Smoker ? ", font=("Helvetica", 16))
SmokerLabel.place(relx=0.1, rely=0.25)
Smoker = Checkbutton(
    addPatientPage, variable=smoke, text="Yes (Checked) / No", font=("Helvetica", 16), onvalue='1', offvalue='0')
Smoker.place(relx=0.2, rely=0.25)

# back btn
backBtn = Button(addPatientPage, text="Back", width=25,
                 command=backButton, bg="red", fg="white", activebackground="#d6252e", activeforeground="white")
backBtn.place(
    relx=1, rely=1, anchor="se")

# add btn
Addbtn = Button(addPatientPage, text="(+) Add Patient", width=25, height=3,
                activebackground='#40a944', activeforeground='white', command=getInfo)
Addbtn.place(relx=0.4, rely=0.5)

# show all records in execl file
exl = Button(addPatientPage, text="open excel file", command=write_to_excel,
             activebackground="lightgreen", activeforeground="black", bg="green", fg="white", width=25)
exl.place(relx=0, rely=1, anchor="sw")

addPatientPage.mainloop()
