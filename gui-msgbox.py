import tkinter

top = tkinter.Tk()

def hello():
   tkinter.messagebox.showinfo("Test", "This is to test message box!")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
