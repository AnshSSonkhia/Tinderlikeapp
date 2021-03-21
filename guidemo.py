from tkinter import *

def check_Login():
    #print(email.get())
    #result.config(text=email.get(), font=("Arial", 20))

    if email.get()=='mridul1998@gmail.com' and password.get()=='1234':
        result.config(text="Welcome", font=("Arial", 30))

    else:
        if email.get() == 'mridul1998@gmail.com' and password.get()!='1234':
            result.config(text="Incorrect password, try again!", font=("Arial", 30))
        else:
            result.config(text="Incorrect email, try again!", font=("Arial", 30))




root=Tk()

root.title("Tinder login")
root.minsize(400,600)
root.maxsize(400,600)

heading=Label(root, text="Login Here")
heading.config(font=("Times", 30))
heading.pack(pady=(30,30))

email_label=Label(root, text="Enter Email:")
email_label.config(font=("Arial",16))
email_label.pack(pady=(10,10))

email=Entry(root)
email.pack(pady=(5,20))

password_label=Label(root, text="Enter password")
password_label.config(font=("Arial",16))
password_label.pack(pady=(5,10))

password=Entry(root)
password.pack(pady=(5,20))

Login=Button(root, text="Login", command=lambda: check_Login())
Login.pack(pady=(10,30))

result=Label(root)
result.pack()
root.mainloop()