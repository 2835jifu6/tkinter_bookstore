from tkinter import *

window=Tk()             #主要window，其他widget要寫在這行和最後一行之中

def km_to_miles():
    gram = float(e1_value.get())*1000
    pound = float(e1_value.get())*2.20462
    ounce = float(e1_value.get())*35.274
    t1.delete("1.0",END)                                #delete從1.0(第一行第0個字節)到END(最後)
    t1.insert(END,gram)                                 #END代表從文字從後面插入
    t2.delete("1.0",END)
    t2.insert(END,pound)
    t3.delete("1.0",END)
    t3.insert(END,ounce)

b1 = Button(window,text="Convert", command=km_to_miles) #設定按鈕
b1.grid(row=0, column=2)                                #設定位置行和列，也可以直接用b1.pack()

e1_value = StringVar()                                  #StringVar()是tkinter專屬的String object，來存String
e1 = Entry(window, textvariable=e1_value)               # 可以輸入文字的地方
e1.grid(row=0, column=1)           

lb = Label(window,text="kg", height=1, width=20)
lb.grid(row=0,column=0)

t1 = Text(window, height=1, width=20)                   #顯示文字
t1.grid(row=1, column=0)
t2 = Text(window, height=1, width=20)                   #顯示文字
t2.grid(row=1, column=1)
t3 = Text(window, height=1, width=20)                   #顯示文字
t3.grid(row=1, column=2)

window.mainloop()
