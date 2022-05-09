from tkinter import *
from tkinter import font

name_list = []
time_list = []
roll_list = []

def save_info():
    firstname_info = firstname.get()
    TIME_info = TIME_text.get()
    TIME_info = int(TIME_info)
    roll_info = roll_num.get()
    if TIME_info < 40:
        name_list.append(firstname_info)
        time_list.append(TIME_info)
        roll_list.append(roll_info)
        file = open("usertext.txt","a")
    
        file.write("student Name :" + firstname_info)
    
        file.write("\n")
        file.write("roll no: " + roll_info)
    
        file.write("\n")
    
        file.write("time spent: " + str(TIME_info))
        file.write("\n")
    
        file.close()

    firstname_entry.delete(0, END)
    TIME_entry.delete(0, END)
    roll_entry.delete(0, END)

screen = Tk()
screen.config(bg="navajo white")
screen.geometry("500x500")
screen.title("ATTENDANCE")
heading = Label(text="ATTENDANCE", bg="navajo white2", fg="black", width="500", height="3", font=("Calisto MT",15,"bold"))
heading.pack()


def print_info():
    root = Toplevel(screen)
    root.geometry("600x600")
    root.title("ABSENTEE LIST")
    root.config(bg="navajo white")
    heading_f = Label(root, text="ABSENTEE LIST", bg="navajo white2", fg="black", width="500", height="3", font=("Calisto MT",15,"bold"))
    heading_f.pack()
    x=[]
    Y=[]
    z=[]
    Label(root, text = "ROLL NUMBER").place(x=50, y= 80)
    Label(root, text="NAME").place(x=300, y=80)
    Label(root, text="TIME PRESENT").place(x=500, y=80)
    for item in range(len(name_list)):
        z.append(Label(root, text= roll_list[item] ))
        z[item].place(x=50, y= 110+(30*item))
        z[item].config()
        x.append(Label(root, text= name_list[item] ))
        x[item].place(x=300, y= 110+(30*item))
        Y.append(Label(root, text= str(time_list[item])))
        Y[item].place(x=500, y=110 + (30 * item))

firstname_text = Label(text="FIRST NAME *", bg="navajo white2")
roll_num = Label(text = "ROLL NUMBER *", bg="navajo white2")
TIME_text = Label(text="TIME PRESENT* ", bg="navajo white2")
firstname_text.place(x=15, y=100)
roll_num.place(x=15, y=170)
TIME_text.place(x=15, y=240)

firstname = StringVar()
TIME_text = IntVar()
roll_num = StringVar()

firstname_entry = Entry(textvariable=firstname, width="60")
TIME_entry = Entry(textvariable=TIME_text, width="60")
roll_entry = Entry(textvariable = roll_num, width = "60")

firstname_entry.place(x=15, y=130)
roll_entry.place(x=15, y=200)
TIME_entry.place(x=15, y=270)

register = Button(screen, text="REGISTER", width="20", height="2", command=save_info, bg="DarkOliveGreen1", font=("HP Simplified Jpan", 11, "bold"))
register.place(x=15, y=380)

finish = Button(screen, text="FINISH", width="20", height="2", command=print_info, bg="brown1", fg="white",font=("HP Simplified Jpan", 11, "bold"))
finish.place(x=270, y=380)
screen.mainloop()