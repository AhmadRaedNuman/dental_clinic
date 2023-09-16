from tkinter import *
from connect import cursor
from tkinter import messagebox
LoginForm = Tk()
LoginForm.title("Login Page")
LoginForm.geometry("300x400")
LoginForm.resizable(False, False)

isLogin = False


def Login():
    global isLogin
    user = username.get()
    password = Password.get()

    sql = f"select * from users where username='{user}' and password='{password}'"
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        isLogin = True
        print('login successful')
        import HomePage

    else:
        print('invalid username or password')
        messagebox.showinfo('Error', 'Invalid Username Or Password')


nameLabel = Label(LoginForm, text="Username: ")
nameLabel.place(relx=0.2, rely=0.2)
username = Entry(LoginForm)
username.place(relx=0.45, rely=0.21)
passwordLabel = Label(LoginForm, text="Password: ")
passwordLabel.place(relx=0.2, rely=0.3)
Password = Entry(LoginForm, show="*")
Password.place(relx=0.45, rely=0.31)
login = Button(LoginForm, width=25, text="Login", bg="#d6252e",
               activebackground="lightgreen", command=Login)
login.place(relx=0.2, rely=0.5)

LoginForm.mainloop()
