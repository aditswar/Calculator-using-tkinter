from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("450x750")
# root.wm_iconbitmap("Python/calculator icon.png")
root.config(background="black")

# few functions
def click(event):
    global display_val  # to change the displayed numbers with an output in end
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if display_val.get().isdigit():
            answer = int(display_val.get())
        else:
            answer = eval(display_val.get())
            display_val.set(answer)
    elif text == "C":
        display_val.set("")
        display.update()
    else:
        display_val.set(display_val.get() + text)
        display.update()

# screen part
display_val = StringVar()
display_val.set("")
display = Entry(root, font="Futura 40 bold", background="grey",foreground="black", text=f"{display_val}")
display.pack(fill=X, pady=10)

frame0 = Frame(root, borderwidth=6, background="black", highlightbackground="black")
frame0.pack(anchor="w")
branding = Label(frame0, text="PY-CALC", font="ROGFonts-Regular 28", bg="black", fg="light grey")
branding.pack(side=LEFT)

# da buttons
frame1 = Frame(root, borderwidth=6, background="grey")
frame1.pack()
b1 = Button(frame1, text="7", font="Futura 40 bold", padx=13, pady=10)
b1.bind("<Button-1>", click)
b1.pack(side=LEFT)
b1 = Button(frame1, text="8", font="Futura 40 bold", padx=13, pady=10)
b1.bind("<Button-1>", click)
b1.pack(side=LEFT)
b1 = Button(frame1, text="9", font="Futura 40 bold", padx=13, pady=10)
b1.bind("<Button-1>", click)
b1.pack(side=LEFT)
b1 = Button(frame1, text="*", font="Futura 40 bold", padx=13, pady=10)
b1.bind("<Button-1>", click)
b1.pack(side=LEFT)

frame2 = Frame(root, borderwidth=6, background="grey")
frame2.pack()
b2 = Button(frame2, text="4", font="Futura 40 bold", padx=13, pady=10)
b2.bind("<Button-1>", click)
b2.pack(side=LEFT)
b2 = Button(frame2, text="5", font="Futura 40 bold", padx=13, pady=10)
b2.bind("<Button-1>", click)
b2.pack(side=LEFT)
b2 = Button(frame2, text="6", font="Futura 40 bold", padx=13, pady=10)
b2.bind("<Button-1>", click)
b2.pack(side=LEFT)
b2 = Button(frame2, text="-", font="Futura 40 bold", padx=14, pady=10)
b2.bind("<Button-1>", click)
b2.pack(side=LEFT)

frame3 = Frame(root, borderwidth=6, background="grey")
frame3.pack()
b3 = Button(frame3, text="1", font="Futura 40 bold", padx=12, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)
b3 = Button(frame3, text="2", font="Futura 40 bold", padx=12, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)
b3 = Button(frame3, text="3", font="Futura 40 bold", padx=11, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)
b3 = Button(frame3, text="+", font="Futura 40 bold", padx=11, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)

frame4 = Frame(root, borderwidth=6, background="grey")
frame4.pack()
b3 = Button(frame4, text="C", font="Futura 35 bold", padx=12, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)
b3 = Button(frame4, text="0", font="Futura 35 bold", padx=12, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)
b3 = Button(frame4, text="%", font="Futura 35 bold", padx=12, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)
b3 = Button(frame4, text="=", font="Futura 35 bold", padx=13, pady=10)
b3.bind("<Button-1>", click)
b3.pack(side=LEFT)

# a close button
close = Button(text="Close", fg="purple", command=root.destroy, bg="white", highlightcolor="grey")
close.pack(side=BOTTOM)
root.mainloop()
