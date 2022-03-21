from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

def operate():
    x=float(a.get())
    powX=int(T.get())
    y=float(b.get())
    powY=int(T2.get())

    if choice.get()=="Addition":
     result = pow(x,powX) + pow(y,powY)
    elif choice.get()=="Subtraction":
     result = pow(x,powX) - pow(y,powY)
    elif choice.get() == "Multiplication":
     result = pow(x, powX) * pow(y, powY)
    else:
     result = pow(x, powX) / pow(y, powY)
    c.set(str(result))

    n=np.arange(0,3,1)
    d=np.array([x,y,result])
    plt.stem(n[0:3], d, 'r--', use_line_collection=True)
    plt.show()
    
root = Tk()
root.title("Calculator")
root.configure(background="#002222",)
root.geometry("1100x500+300+100")




a=DoubleVar()
a.set(" ")
b=DoubleVar()
b.set(" ")
c=DoubleVar()
c.set(" ")
T = IntVar()
T.set(1)
T2 = IntVar()
T2.set(1)

power = [
    ["^1", 1],
    ["^2", 2],
    ["^3", 3],
    ["^4", 4],
    ["^5", 5]
]

Label(root, text="First Number", fg = "#EEEEFF",bg = "#002222", font = ("bold",20)).grid(row=0,column=0,padx=(100,0),pady=(100,0))
Entry(root, textvariable=a,  width=20,font = "Times 20 bold italic",).grid(row=0, column=1, padx=5,pady=(100,0))

for text, mode in power:
    Radiobutton(root, text=text, variable=T,value=mode, fg="#002222",bg="#DDDDDD",font = ("bold",20), activeforeground = "#002222",  activebackground="#DDDDDD").grid(row=0, column=mode+1,pady=(100,0))

Label(root, text="Second Number",fg = "#EEEEFF", bg = "#002222", font = ("bold",20)).grid(row=1,column=0,padx=(100,0))
Entry(root, textvariable=b, width=20,font = "Times 20 bold italic",).grid(row=1, column=1, padx=5)

for text, mode in power:
    Radiobutton(root, text=text, variable=T2,value=mode, fg="#002222",bg="#DDDDDD",font = ("bold",20), activeforeground = "#002222",  activebackground="#DDDDDD").grid(row=1, column=mode+1)






choice = StringVar()
choice.set("Addition")
options_to=[
                       "Addition",
                       "Subtraction",
                       "Multiplication",
                       "Division",

]

drop_to = OptionMenu(root, choice, *options_to)
drop_to.config(fg = "#777777", font = ("bold",20))

drop_to.grid(row=3, column=1, pady=(10,0))
Button(root,text = "Show answer",fg = "#777700",bg="#FFFFCC",border = "4px",font = "Times 20 bold italic",command = operate).grid(row=4, column=1, pady=(10,0))
Label(root, textvariable=c, height = 1, width=20,font = "Times 20 bold italic",).grid(row=5, column=1, padx=5)


root.mainloop()

