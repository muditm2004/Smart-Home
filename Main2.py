from tkinter import *
from pygame import mixer as mix


root = Tk()
root.title("Smart Home by")
root.geometry("1000x700")
root.resizable(0,0)

mix.init()


off_file=PhotoImage(file="off.png")
on_left_file=PhotoImage(file="on_left.png")
on_right_file=PhotoImage(file="on_right.png")

bar_on_file=PhotoImage(file="bar_on.png")
kitchen_on_file=PhotoImage(file="kitchen_on.png")
theatre_on_file=PhotoImage(file="theatre_on.png")
bedroom_on_file=PhotoImage(file="bedroom_on.png")


def on_enter_frame2(event):
    global on_left_file
    global bedroom_on_file
    on_left=Label(frame2,image=on_left_file,borderwidth=0)
    on_left.place(x=165,y=17)
    bedroom_on=Label(bedroom,image=bedroom_on_file,borderwidth=0)
    bedroom_on.place(x=0,y=0)
    
def on_leave_frame2(event):
    global off_file
    global bedroombgfile
    off=Label(frame2,image=off_file,borderwidth=0)
    off.place(x=165,y=17)
    bedroombg=Label(bedroom,image=bedroombgfile,borderwidth=0)
    bedroombg.place(x=0,y=0)

def on_enter_frame3(event):
    global on_right_file
    global theatre_on_file
    on_right=Label(frame3,image=on_right_file,borderwidth=0)
    on_right.place(x=165,y=17)
    theatrebg=Label(Theatre,image=theatre_on_file,borderwidth=0)
    theatrebg.place(x=0,y=0)
    mix.music.load('Netflix-Intro.mp3')
    mix.music.play()

def on_leave_frame3(event):
    global off_file
    global Theatrebgfile
    off=Label(frame3,image=off_file,borderwidth=0)
    off.place(x=165,y=17)
    Theatrebg=Label(Theatre,image=Theatrebgfile,borderwidth=0)
    Theatrebg.place(x=0,y=0)
    mix.music.load('Netflix-Intro.mp3')
    mix.music.pause()

def on_enter_frame4(event):
    global on_left_file
    global bar_on_file
    on_left=Label(frame4,image=on_left_file,borderwidth=0)
    on_left.place(x=165,y=17)
    barbg=Label(Bar,image=bar_on_file,borderwidth=0)
    barbg.place(x=0,y=0)
    mix.music.load('Bar Music.mp3')
    mix.music.play() 
    
def on_leave_frame4(event):
    global off_file
    global barbgfile
    off=Label(frame4,image=off_file,borderwidth=0)
    off.place(x=165,y=17)
    barbg=Label(Bar,image=barbgfile,borderwidth=0)
    barbg.place(x=0,y=0)
    mix.music.load('Bar Music.mp3')
    mix.music.pause()

def on_enter_frame5(event):
    global on_right_file
    global kitchen_on_file
    on_right=Label(frame5,image=on_right_file,borderwidth=0)
    on_right.place(x=165,y=17)
    kitchenbg=Label(kitchen,image=kitchen_on_file,borderwidth=0)
    kitchenbg.place(x=0,y=0)

def on_leave_frame5(event):
    global off_file
    global kitchenbgfile
    off=Label(frame5,image=off_file,borderwidth=0)
    off.place(x=165,y=17)
    kitchenbg=Label(kitchen,image=kitchenbgfile,borderwidth=0)
    kitchenbg.place(x=0,y=0)


# Create left frames
frame1 = Frame(root, bg="black", width=500, height=100)
frame1bgfile=PhotoImage(file="frame1bg.png")
frame1bg=Label(frame1,image=frame1bgfile,borderwidth=0)
frame1bg.grid(row=0,column=0)

frame2 = Frame(root, bg="black", width=500, height=125)
frame2bgfile=PhotoImage(file="frame2bg.png")
frame2bg=Label(frame2,image=frame2bgfile,borderwidth=0)
frame2bg.grid(row=1,column=0)

frame3 = Frame(root, bg="black", width=500, height=125)
frame3bgfile=PhotoImage(file="frame3bg.png")
frame3bg=Label(frame3,image=frame3bgfile,borderwidth=0)
frame3bg.grid(row=2,column=0)

frame4 = Frame(root, bg="black", width=500, height=125)
frame4bgfile=PhotoImage(file="frame4bg.png")
frame4bg=Label(frame4,image=frame4bgfile,borderwidth=0)
frame4bg.grid(row=3,column=0)

frame5 = Frame(root, bg="black", width=500, height=125)
frame5bgfile=PhotoImage(file="frame5bg.png")
frame5bg=Label(frame5,image=frame5bgfile,borderwidth=0)
frame5bg.grid(row=4,column=0)

frame6 = Frame(root, bg="black", width=500, height=100)
frame6bgfile=PhotoImage(file="frame6bg.png")
frame6bg=Label(frame6,image=frame6bgfile,borderwidth=0)
frame6bg.grid(row=5,column=0)




ground_room= Frame(root, bg="green", width=500, height=100)
ground_roombgfile=PhotoImage(file="groundbg.png")
ground_roombg=Label(ground_room,image=ground_roombgfile,borderwidth=0)
ground_roombg.grid(row=5,column=2)

kitchen= Frame(root, bg="white", width=500, height=125)
kitchenbgfile=PhotoImage(file="kitchenbg.png")
kitchenbg=Label(kitchen,image=kitchenbgfile,borderwidth=0)
kitchenbg.grid(row=4,column=2)

Bar= Frame(root, bg="blue", width=500, height=125)
barbgfile=PhotoImage(file="barbg.png")
barbg=Label(Bar,image=barbgfile,borderwidth=0)
barbg.grid(row=3,column=2)

Theatre= Frame(root, bg="red", width=500, height=125)
Theatrebgfile=PhotoImage(file="Theatrebg.png")
Theatrebg=Label(Theatre,image=Theatrebgfile,borderwidth=0)
Theatrebg.grid(row=2,column=2)

bedroom= Frame(root, bg="blue", width=500, height=125)
bedroombgfile=PhotoImage(file="bedroombg.png")
bedroombg=Label(bedroom,image=bedroombgfile,borderwidth=0)
bedroombg.grid(row=1,column=2)

terrace= Frame(root, bg="pink", width=500, height=100)
terracebgfile=PhotoImage(file="terrace.png")
terracebg=Label(terrace,image=terracebgfile,borderwidth=0)
terracebg.grid(row=0,column=2)




# Use the grid geometry manager to divide the window into 2 rows and 2 columns
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=2, column=0)
frame4.grid(row=3, column=0)
frame5.grid(row=4, column=0)
frame6.grid(row=5, column=0)

ground_room.grid(row=5, column=1)
kitchen.grid(row=4, column=1)
Bar.grid(row=3, column=1)
Theatre.grid(row=2, column=1)
bedroom.grid(row=1, column=1)
terrace.grid(row=0, column=1)


# Bind the <Enter> and <Leave> events to the corresponding functions
frame2.bind("<Enter>", on_enter_frame2)
frame2.bind("<Leave>", on_leave_frame2)
frame3.bind("<Enter>", on_enter_frame3)
frame3.bind("<Leave>", on_leave_frame3)
frame4.bind("<Enter>", on_enter_frame4)
frame4.bind("<Leave>", on_leave_frame4)
frame5.bind("<Enter>", on_enter_frame5)
frame5.bind("<Leave>", on_leave_frame5)

root.mainloop()