import tkinter
import sqlite3
conn=sqlite3.connect("MDBA.db")
rootAA=None

def set():
    global e3,e1,e2,e4,e5,e6,conn
    p1=e1.get()
    p2=e2.get()
    p3=e3.get(tkinter.ACTIVE)
    p4=e4.get()
    p5=e5.get()
    p6=e6.get(1.0,tkinter.END)
    conn = sqlite3.connect("MDBA.db")
    conn.execute("Insert into appointment values(?,?,?,?,?,?)",(p1,p2,p3,p4,p5,p6,))
    conn.commit()
    tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")


def appo():
    global rootAA,L,e1,e2,e3,e4,e5,e6
    rootAA=tkinter.Tk()
    rootAA.geometry("1000x850")
    rootAA.title("APPOINTMENTS")
    H=tkinter.Label(rootAA,text="APPOINTMENTS",fg="blue",font="Arial 25 bold")
    H.place(x=340,y=20)
    l1=tkinter.Label(rootAA,text="PATIENT ID",font="Arial 11")
    l1.place(x=200,y=95)
    e1=tkinter.Entry(rootAA)
    e1.place(x=320,y=95)
    l2 = tkinter.Label(rootAA,text="DOCTOR ID",font="Arial 11")
    l2.place(x=200,y=130)
    e2 = tkinter.Entry(rootAA)
    e2.place(x=320,y=130)
    l3 = tkinter.Label(rootAA,text="APPOINTMENT NO",font="Arial 11")
    l3.place(x=200,y=165)
    L=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50']
    e3=tkinter.Listbox(rootAA, width=15, height=1, selectmode='SINGLE', exportselection=0)
    for jjj in L:
        e3.insert(tkinter.END, jjj)
    e3.place(x=370,y=165)
    l4 = tkinter.Label(rootAA,text="APPOINTMENT TIME(HH:MM)",font="Arial 11")
    l4.place(x=200,y=200)
    e4=tkinter.Entry(rootAA)
    e4.place(x=470,y=200)
    l5 = tkinter.Label(rootAA,text="APPOINTMENT DATE(YYYY-MM-DD)",font="Arial 11")
    l5.place(x=200,y=235)
    e5=tkinter.Entry(rootAA)
    e5.place(x=530,y=235)
    l6=tkinter.Label(rootAA,text="DESCRIPTION",font="Arial 11")
    l6.place(x=200,y=270)
    e6=tkinter.Text(rootAA,width=30,height=5)
    e6.place(x=200,y=300)
    scrollbar = tkinter.Scrollbar(rootAA,orient=tkinter.HORIZONTAL)
    scrollbar.place(x=500,y=165)
    e3.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=e3.yview)
    b1=tkinter.Button(rootAA,text="SET APPOINTMENT",command=set,font="Arial 13 bold")
    b1.place(x=130,y=450)
    b2=tkinter.Button(rootAA,text="DELETE APPOINTMENT",command=dela,font="Arial 13 bold")
    b2.place(x=380,y=450)
    b4=tkinter.Button(rootAA,text="TODAYS APPOINTMENTS",command=va,font="Arial 13 bold")
    b4.place(x=670,y=450)
    rootAA.mainloop()


def remove():
    global e7,edd
    edd=str(e7.get())
    v=list(conn.execute("select * from appointment where AP_NO=?", (edd,)))
    if (len(v)==0):
        errorD = tkinter.Label(rootAA, text="PATIENT APPOINTMENT NOT FIXED",fg="red")
        errorD.place(x=20,y=420)
    else:
        conn.execute('DELETE FROM PATIENT where PATIENT_ID=?',(edd,))
        disd1=tkinter.Label(rootAA,text="PATIENT APPOINTMENT DELETED",fg='green')
        disd1.place(x=20,y=420)
        conn.commit()



def dela():
    global e1,e7
    l3 = tkinter.Label(rootAA, text="ENTER APPOINTMENT NO TO DELETE")
    l3.place(x=20, y=340)
    e7=tkinter.Entry(rootAA)
    e7.place(x=20,y=360)
    b3=tkinter.Button(rootAA,text="Delete",command=remove)
    b3.place(x=50,y=380)

rootAP=None

def viewappointment():
    global e8
    ap=str(e8.get())
    vv = list(conn.execute("select * from appointment where AP_DATE=?", (ap,)))
    if (len(vv) == 0):
        errorD = tkinter.Label(rootAA, text="NO APPOINTMENT FOR TODAY", fg="red",font="Arial 10 bold")
        errorD.place(x=20, y=420)
    else:
        s=conn.execute("Select PATIENT_ID,Patient_name,AP_NO,EMP_NAME,AP_DATE,AP_TIME from PATIENT NATURAL JOIN employee NATURAL JOIN appointment where AP_DATE=?",(ap,))
        for i in s:
            s1=tkinter.Label(rootAP,text=i[0],fg='green')
            s1.place(x=10,y=85)
            s1.pack()


def va():
    global rootAP,e8
    rootAP=tkinter.Tk()
    rootAP.geometry("500x550")
    rootAP.title("TODAYS APPOINTMENTS")
    h1=tkinter.Label(rootAP,text="ENTER DATE TO VIEW APPOINTMENTS")
    h1.place(x=20,y=20)
    e8=tkinter.Entry(rootAP)
    e8.place(x=20,y=40)
    b5=tkinter.Button(rootAP,text="SEARCH",command=viewappointment)
    b5.place(x=30,y=65)
    rootAP.mainloop()

