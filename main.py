from tkinter import *

root = Tk()
root.geometry("320x535+200+100")
root.title("Calculator by Dev")
root.iconbitmap("cal.ico")
root.resizable(0, 0)

# Click function


def click(event):
    global var_value
    text = event.widget.cget("text")
    if text == "    =    ":
        if var_value.get().isdigit():
            value = int(var_value.get())
        else:
            try:
                value = eval(display.get())
            except Exception as e:
                print(e)
                value = "Error"
            var_value.set(value)
            display.update()

    elif text == "c":
        var_value.set("")
        display.update()

    elif text == " .":
        display.insert(END, ".")
        return

    else:
        var_value.set(var_value.get() + str(text))
        display.update()


var_value = StringVar()
var_value.set("")

display = Entry(root, textvar=var_value, font="lucida 30", justify=RIGHT, relief=SOLID)
display.pack(padx=10, pady=20, ipady=2, ipadx=5)

f1 = Frame(root, bg="grey")
list5 = ['( ', ' )', 'c', " /"]
for i in list5:
    btn = Button(f1, text=i, font="lucida 30 bold", padx=7, bg="aliceblue")
    btn.pack(side=LEFT, padx=2, pady=2)
    btn.bind("<Button-1>", click)
f1.pack(side=TOP, padx=12)

f = Frame(root, bg="grey")
list1 = [7, 8, 9, " *"]
for i in list1:
    btn = Button(f, text=i, font="lucida 30 bold", padx=6.5, bg="aliceblue")
    btn.pack(side=LEFT, padx=2, pady=2)
    btn.bind("<Button-1>", click)
f.pack(side=TOP, padx=12)

f = Frame(root, bg="grey")
list2 = [4, 5, 6, " -"]
for j in list2:
    btn = Button(f, text=j, font="lucida 30 bold", padx=7, bg="aliceblue")
    btn.pack(side=LEFT, padx=2, pady=2)
    btn.bind("<Button-1>", click)
f.pack(side=TOP, padx=12)

f = Frame(root, bg="grey")
list3 = [1, 2, 3, " +"]
for i in list3:
    btn = Button(f, text=i, font="lucida 30 bold", padx=7, bg="aliceblue")
    btn.pack(side=LEFT, padx=1.5, pady=2)
    btn.bind("<Button-1>", click)
f.pack(side=TOP, padx=12)

f = Frame(root, bg="grey")
list4 = [' .', 0, "    =    "]
for k in list4:
    btn = Button(f, text=k, font="lucida 30 bold", padx=7, bg="aliceblue")
    btn.pack(side=LEFT, padx=1.5, pady=2)
    btn.bind("<Button-1>", click)
f.pack(side=TOP, padx=12)

root.mainloop()
