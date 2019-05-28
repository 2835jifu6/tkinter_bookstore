from tkinter import *

window=Tk()             #主要window，其他widget要寫在這行和最後一行之中

b1 = Button(window,text="Execute") #設定按鈕
b1.grid(row=0, column=0)           #設定位置行和列，也可以直接用b1.pack()

e1 = Entry(window)
e1.grid(row=0, column=1)           #可以輸入文字的地方

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()