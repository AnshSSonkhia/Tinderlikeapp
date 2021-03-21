from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from dbhelper import DBhelper


class Tinder:

    def __init__(self):

        self.db=DBhelper()

        self.load_login_window()

    def load_login_window(self):
        
        self._root = Tk()

        self._root.title("Tinder Login")
        self._root.minsize(400, 600)
        self._root.maxsize(400, 600)
        self._root.config(background="#F60A40", )

        self._label1 = Label(self._root, text="Tinder", fg="#fff", bg="#F60A40")
        self._label1.config(font=("Arial", 30))
        self._label1.pack(pady=(10, 15))

        self._email = Label(self._root, text="Enter Email", fg="#fff", bg="#F60A40")
        self._email.config(font=("Times", 20))
        self._email.pack(pady=(10, 10))

        self._emailinput = Entry(self._root)
        self._emailinput.pack(pady=(5, 25), ipady=10, ipadx=26)

        self._password = Label(self._root, text="Enter Password", fg="#fff", bg="#F60A40")
        self._password.config(font=("Times", 20))
        self._password.pack(pady=(10, 10))

        self._passwordinput = Entry(self._root)
        self._passwordinput.pack(pady=(5, 25), ipady=10, ipadx=26)

        self._login = Button(self._root, text="Login", width=15, height=2, command=lambda: self.check_login())
        self._login.pack(pady=(10, 10))

        self._reg = Button(self._root, text="Sign up", width=15, height=2, command=lambda: self.regWindow())
        self._reg.pack(pady=(5, 5))

        self._root.mainloop()



    def check_login(self):
        email = self._emailinput.get()
        password = self._passwordinput.get()

        data=self.db.check_login(email, password)

        #print(data)
        if len(data)==0:
            messagebox.showerror("Error","Invalid credentials")
           # print("invalid credentials")

        else:
            self.user_id=data[0][0]
            self.is_logged_in=1
            self.login_handler()

    def regWindow(self):

        self.clear()

        self._name = Label(self._root, text="Name", fg="#fff", bg="#F60A40")
        self._name.config(font=("Times", 16))
        self._name.pack(pady=(5, 5))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._email = Label(self._root, text="Email", fg="#fff", bg="#F60A40")
        self._email.config(font=("Times", 16))
        self._email.pack(pady=(5, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#F60A40")
        self._password.config(font=("Times", 16))
        self._password.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._gender = Label(self._root, text="Gender", fg="#fff", bg="#F60A40")
        self._gender.config(font=("Times", 16))
        self._gender.pack(pady=(5, 5))

        self._genderInput = Entry(self._root)
        self._genderInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._age = Label(self._root, text="Age", fg="#fff", bg="#F60A40")
        self._age.config(font=("Times", 16))
        self._age.pack(pady=(5, 5))

        self._ageInput = Entry(self._root)
        self._ageInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._city = Label(self._root, text="City", fg="#fff", bg="#F60A40")
        self._city.config(font=("Times", 16))
        self._city.pack(pady=(5, 5))

        self._cityInput = Entry(self._root)
        self._cityInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._reg = Button(self._root, text="Sign Up", bg="#fff", width=25, height=2, command=lambda: self.reg_handler())
        self._reg.pack(pady=(10, 10))

    def reg_handler(self):

        flag = self.db.register(self._nameInput.get(), self._emailInput.get(), self._passwordInput.get(),
                                self._ageInput.get(), self._genderInput.get(), self._cityInput.get())

        if flag == 1:
            messagebox.showerror("Success", "Registered Successfully.Login to proceed")
            self._root.destroy()
            self.load_login_window()
        else:
            messagebox.showerror("Error", "Try again!")
    def mainwindow(self, data,flag=0,index=0):

        imageUrl = "images/p.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()



        name = "Name: " + str(data[index][1])
        email = "Email: " + str(data[index][2])
        age = "Age: " + str(data[index][4])
        gender = "Gender: " + str(data[index][5])
        city = "City: " + str(data[index][6])
       # DP="Dp: "+ str(data[index][7])

        name_label = Label(self._root, text=name, fg="#fff", bg="#F60A40")
        name_label.config(font=("Arial", 14))
        name_label.pack(pady=(20, 10))

        email_label = Label(self._root, text=email, fg="#fff", bg="#F60A40")
        email_label.config(font=("Arial", 14))
        email_label.pack(pady=(5, 10))

        age_label = Label(self._root, text=age, fg="#fff", bg="#F60A40")
        age_label.config(font=("Arial", 14))
        age_label.pack(pady=(5, 10))

        gender_label = Label(self._root, text=gender, fg="#fff", bg="#F60A40")
        gender_label.config(font=("Arial", 14))
        gender_label.pack(pady=(5, 10))

        city_label = Label(self._root, text=city, fg="#fff", bg="#F60A40")
        city_label.config(font=("Arial", 14))
        city_label.pack(pady=(5, 10))

        # DP_label = Label(self._root, text=DP, fg="#fff", bg="#F60A40")
         #DP_label.config(font=("Arial", 14))
        # DP_label.pack(pady=(5, 10))

        if flag==1:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="Previous",command=lambda : self.view_others(index-1))
            previous.pack(side=LEFT)

            propose = Button(frame, text="Propose",command=lambda: self.propose(self.user_id, data[index][0]))
            propose.pack(side=LEFT)

            next = Button(frame, text="Next",command=lambda : self.view_others(index+1))
            next.pack(side=LEFT)

        elif flag==2:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="Previous", command=lambda: self.view_proposals(index - 1))
            previous.pack(side=LEFT)

            propose = Button(frame, text="Propose", command=lambda: self.propose(self.user_id, data[index][0]))
            propose.pack(side=LEFT)

            next = Button(frame, text="Next", command=lambda: self.view_proposals(index + 1))
            next.pack(side=LEFT)

        elif flag==3:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="Previous", command=lambda: self.view_proposals(index - 1))
            previous.pack(side=LEFT)

            #propose = Button(frame, text="Propose", command=lambda: self.propose(self.user_id, data[index][0]))
            #propose.pack(side=LEFT)

            next = Button(frame, text="Next", command=lambda: self.view_proposals(index + 1))
            next.pack(side=LEFT)

        elif flag == 4:
            frame = Frame(self._root)
            frame.pack()

            previous = Button(frame, text="Previous", command=lambda: self.view_proposals(index - 1))
            previous.pack(side=LEFT)

            # propose = Button(frame, text="Propose", command=lambda: self.propose(self.user_id, data[index][0]))
            # propose.pack(side=LEFT)

            next = Button(frame, text="Next", command=lambda: self.view_proposals(index + 1))
            next.pack(side=LEFT)


    def propose(self, romeo, juliet):
        flag=self.db.insert_proposal(romeo,juliet)

        if flag==1:
            messagebox.showinfo("congrats","proposal sent.Fingers crossed")
        elif flag==2:
            messagebox.showinfo("proposal already sent!")
        else:
            messagebox.showinfo("oops! something wrong, try again")



    def login_handler(self):
        self.clear()
        self.headerMenu()
        data = self.db.fetch_userdata(self.user_id)
        self.mainwindow(data)



    def clear(self):
        for i in self._root.pack_slaves():
            print(i.destroy())

    def view_others(self, index=0):

        data=self.db.fetch_otheruserdata(self.user_id)

        if index==0:
            self.clear()
            self.mainwindow(data, flag=1,index=0)
        else:
            if index<0:

                messagebox.showerror("No User found","Click on Next")
            elif index==len(data):
                messagebox.showerror("No User found", "Click on Previous")

            else:
                self.clear()
                self.mainwindow(data, flag=1, index=index)
    def logout(self):
        self.is_logged_in=0
        self._root.destroy()
        self.load_login_window()

    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: self.login_handler())
        filemenu.add_command(label="Edit Profile")
        filemenu.add_command(label="View Profile", command=lambda: self.view_others())
        filemenu.add_command(label="LogOut", command=lambda: self.logout())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command=lambda: self.view_proposals())
        helpmenu.add_command(label="My Requests", command=lambda: self.view_requests())
        helpmenu.add_command(label="My Matches",command=lambda: self.view_matches())

    def view_proposals(self,index=0):

        data=self.db.fetch_proposals(self.user_id)

        new_data=[]
        for i in data:
            new_data.append(i[3:])

        if index==0:
            self.clear()
            self.mainwindow(new_data, flag=2, index=0)
        else:
            if index<0:

                messagebox.showinfo("oops!" ,"No user found")
            elif index==len(new_data):
                messagebox.showinfo("oops! " ,"No user found")
            else:
                self.clear()
                self.mainwindow(new_data, flag=2, index=index)

    def view_requests(self, index=0):

        data = self.db.fetch_requests(self.user_id)

        new_data = []
        for i in data:
            new_data.append(i[3:])

        if index == 0:
            self.clear()
            self.mainwindow(new_data, flag=3, index=0)
        else:
            if index < 0:

                messagebox.showinfo("oops!", "No user found")
            elif index == len(new_data):
                messagebox.showinfo("oops! ", "No user found")
            else:
                self.clear()
                self.mainwindow(new_data, flag=3, index=index)

    #print(new_data)

    def view_matches(self, index=0):

        data = self.db.fetch_matches(self.user_id)

        new_data = []
        for i in data:
            new_data.append(i[3:])

        if index == 0:
            self.clear()
            self.mainwindow(new_data, flag=4, index=0)
        else:
            if index < 0:

                messagebox.showinfo("oops!", "No user found")
            elif index == len(new_data):
                messagebox.showinfo("oops! ", "No user found")
            else:
                self.clear()
                self.mainwindow(new_data, flag=4, index=index)





obj=Tinder()

