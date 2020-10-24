from tkinter import *
from user import *

class data:
    def __init__(self):
        self.floor = None
        self.type = None

    def setfloor(self,floor,type):
        self.floor = floor
        self.type = type

def gotofloor(floor,root):
    #     port = '/dev/ttyS0'
    #     ard = serial.Serial(port, 9600, timeout=5)
    #     ard.write(floor)
    #     time.sleep(4)
    root.destroy()
    print(floor, "floor")
    pass

def user_GUI(name):
    root = Tk()
    pad=0
    # root.geometry("1024x600")
    root.geometry("{0}x{1}".format(
        root.winfo_screenwidth() - pad, root.winfo_screenheight() - pad))
    root.wm_attributes('-type', 'splash')
    frame = Frame(root)
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    str = "Welcome " + name
    label = Label(frame,text = str)
    label.config(width=200)
    label.config(font=("MS Serif", 90))
    label.pack()
    root.after(1500, root.destroy)
    root.mainloop()

def admin_GUI():
    root = Tk()
    pad = 0
    dt = data()
    # root.geometry("1024x600")
    height = root.winfo_screenheight() - pad
    width = root.winfo_screenwidth() - pad
    root.geometry("{0}x{1}".format(width, height))
    root.wm_attributes('-type', 'splash')
    admin_frame = Frame(root, bg="green")
    btn_height = int(height/3)
    btn_width = int(width /3)
    btn1 = Button(admin_frame, text="1", command=lambda: gotofloor(1,root), height=8, width=60)
    btn1.grid(column=0, row=0)
    btn2 = Button(admin_frame, text="2", command=lambda: gotofloor(2,root), height=8, width=60)
    btn2.grid(column=1, row=0)

    btn3 = Button(admin_frame, text="3", command=lambda: gotofloor(3,root), height=8, width=60)
    btn3.grid(column=0, row=1)
    btn4 = Button(admin_frame, text="4", command=lambda: gotofloor(4,root), height=8, width=60)
    btn4.grid(column=1, row=1)

    btn5 = Button(admin_frame, text="5", command=lambda: gotofloor(5,root), height=8, width=60)
    btn5.grid(column=0, row=2)
    add_btn = Button(admin_frame, text="Add User",command=lambda:adduser(root,admin_frame,dt), height=8, width=60)
    add_btn.grid(column=1, row=2)
    admin_frame.grid()
    root.mainloop()
    return dt

def goback(root):
    root.destroy()
    admin_GUI()

def submit(root,floor,dt,type):
    root.destroy()
    dt.floor = floor
    dt.type = type
    print("here")

def adduser(root,frame,dt):
    frame.destroy()
    new_frame = Frame(root)
    new_frame.grid()
    type="user"
    back_btn = Button(new_frame, text="Back", command=lambda: goback(root), height=12, width=20)
    back_btn.grid(column=0, row=0)

    # lab = Label(new_frame, text="Name :", height=5)
    # te = Entry(new_frame)
    #
    # lab.grid(column=0, row=1)
    # te.grid(column=1, row=1)

    floor = Label(new_frame, text="Pick floor:", height=5)
    box = Spinbox(new_frame, from_=1, to=5)
    floor.grid(column=0, row=2)
    box.grid(column=1, row=2)

    sub_btn = Button(new_frame, text="Submit",command=lambda:submit(root,box.get(),dt,type), height=12, width=20)
    sub_btn.grid(column=0, row=3)
