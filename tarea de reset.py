from tkinter import*


def resetear():
    opcion.set(None)


window = Tk()
seleccion=StringVar()
opcion=StringVar()
opcion.set(None)
Radiobutton(window,text="a+b",variable=opcion,
            value="a+b",command=seleccion).pack(anchor=W)
Radiobutton(window,text="a-b",variable=opcion,
            value="a-b",command=seleccion).pack(anchor=W)
Radiobutton(window,text="a*b",variable=opcion,
            value="a*b",command=seleccion).pack(anchor=W)
Radiobutton(window,text="a/b",variable=opcion,
            value="a/b",command=seleccion).pack(anchor=W)

Button(window,text="reset",command=resetear,padx=5,pady=5).pack()
window.mainloop()

