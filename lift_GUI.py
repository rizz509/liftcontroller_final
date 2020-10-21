from tkinter import *

def gotofloor(floor):
    #     port = '/dev/ttyS0'
    #     ard = serial.Serial(port, 9600, timeout=5)
    #     ard.write(floor)
    #     time.sleep(4)
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
    root.after(1000, root.destroy)
    root.mainloop()

def admin_GUI():
    root = Tk()
    pad = 0
    # root.geometry("1024x600")
    height = root.winfo_screenheight() - pad
    width = root.winfo_screenwidth() - pad
    root.geometry("{0}x{1}".format(width, height))
    root.wm_attributes('-type', 'splash')
    admin_frame = Frame(root, bg="green")
    btn_height = int(height/3)
    btn_width = int(width /3)
    btn1 = Button(admin_frame, text="1", command=lambda: gotofloor(1))#, height=btn_height, width=btn_width)
    #btn1.config(font=("MS Serif", 8))
    btn1.grid(column=0, row=0,columnspan = btn_width,rowspan=btn_height)
    btn2 = Button(admin_frame, text="2", command=lambda: gotofloor(2))#, height=btn_height, width=btn_width)
    #btn2.config(font=("MS Serif", 8))
    btn2.grid(column=1, row=0,columnspan = btn_width,rowspan=btn_height)

    btn3 = Button(admin_frame, text="3", command=lambda: gotofloor(3))#, height=btn_height,width=btn_width)
    #btn3.config(font=("MS Serif", 8))
    btn3.grid(column=0, row=1,columnspan = btn_width,rowspan=btn_height)
    btn4 = Button(admin_frame, text="4", command=lambda: gotofloor(4))#, height=btn_height, width=btn_width)
    #btn4.config(font=("MS Serif", 8))
    btn4.grid(column=1, row=1,columnspan = btn_width,rowspan=btn_height)

    btn5 = Button(admin_frame, text="5", command=lambda: gotofloor(5))#, height=btn_height, width=btn_width)
    #btn5.config(font=("MS Serif", 8))
    btn5.grid(column=0, row=2,columnspan = btn_width,rowspan=btn_height)
    add_btn = Button(admin_frame, text="Add User")#,  height=btn_height, width=btn_width)
    #add_btn.config(font=("MS Serif", 8))
    add_btn.grid(column=1, row=2,columnspan = btn_width,rowspan=btn_height)
    admin_frame.grid()
    root.mainloop()

admin_GUI()