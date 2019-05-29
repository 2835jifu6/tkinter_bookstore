import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")     #建立連線
    cur=conn.cursor()                   #建立cursor物件，這樣才可以取得資料庫的資料
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #SOL指令，table名稱為store，欄位名為item(String)，quantity(integer)和price(float)
    conn.commit()  #提交database的改變
    conn.close()   #連線要關閉

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

create_table()
insert("glass",10,2)
print(view())