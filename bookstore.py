from tkinter import *

window=Tk()             #主要window，其他widget要寫在這行和最後一行之中

def km_to_miles():
    mile = float(e1_value.get())*1.6
    t1.insert(END,mile)                                 #END代表從文字從後面插入

b1 = Button(window,text="Execute", command=km_to_miles) #設定按鈕
b1.grid(row=0, column=0)                                #設定位置行和列，也可以直接用b1.pack()

e1_value = StringVar()                                  #StringVar()是tkinter專屬的String object，來存String
e1 = Entry(window, textvariable=e1_value)               # 可以輸入文字的地方
e1.grid(row=0, column=1)           

t1 = Text(window, height=1, width=20)                   #顯示文字
t1.grid(row=0, column=2)

window.mainloop()
