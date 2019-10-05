import tkinter
from window2 import menu
import sqlite3

#root=login page
#root1=menu
#rootp=patient form

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None

conn=sqlite3.connect("MDBA.db")
cursor=conn.cursor()
print("DATABASE CONNECTION SUCCESSFUL")

#command for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    query = "select * from Login where username=? and password=?"
    data = cursor.execute(query, (S1, S2))
    if (len(cursor.fetchall()) > 0):
        menu()
    else:
        error = tkinter.Label(bottomframe, text="Wrong Id / Password \n TRY AGAIN", fg="red", font='Times 16 bold')
        error.pack()
    '''if(S1=='sanjyot' and S2=='1234567'):
        menu()
    elif(S1=='abhish' and S2=='btech'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()'''


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("1000x850")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO SOA CLINIC",bg='white',fg='orange',font='Times 32 bold italic')
    username=tkinter.Label(topframe,text="USERNAME",font='12')
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="PASSWORD",font='12')
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font="arial 12 bold")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

