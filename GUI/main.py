import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

from tkinter import *

root = Tk()

root.geometry("500x500")

root.title('Email Manager')

label_0 =Label(root,text="Email Manager", width=20,font=("bold",20))
label_0.place(x=90,y=60)

label_1 =Label(root,text="Your Email", width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1=Entry(root)
entry_1.place(x=240,y=140)

label_5 =Label(root,text="Reciever Email", width=20,font=("bold",10))
label_5.place(x=50,y=300)

entry_5=Entry(root)
entry_5.place(x=240,y=300)


label_6 =Label(root,text="Subject", width=20,font=("bold",10))

label_6.place(x=50,y=350)
entry_6=Entry(root)
entry_6.place(x=240,y=350)
label_3 =Label(root,text="Password", width=20,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root, show='*')
entry_3.place(x=240,y=180)

label_2 =Label(root,text="Message", width=20,font=("bold",10))
label_2.place(x=70,y=230)

entry_2=Entry(root)
entry_2.place(x=240,y=230, height=50)

def send_mail():
    server.login(entry_1.get(), entry_3.get())
    server.sendmail(entry_1.get(), entry_5.get(), f"Subject:{entry_6.get()}\n\n {entry_2.get()}")
Button(root, text='Submit' , width=20,bg="black",fg='white', command=send_mail).place(x=180,y=400)

root.mainloop()
