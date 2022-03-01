import tkinter

window = tkinter.Tk()
window.title("my first GUI Program")
window.minsize(width=500,height=300)


my_label = tkinter.Label(text="I am a Label", font=("Ariel",24,"bold"))
my_label.pack()