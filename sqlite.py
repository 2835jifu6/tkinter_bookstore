import sqlite3
import psycopg2
#sqlite3和psycopg2語法相似，差別在於一開始connect的部分和占位符的使用

def create_table():
    #conn=sqlite3.connect("lite.db")     sqlite3建立連線
    conn=psycopg2.connect("dbname='python_use' user='postgres' password='04500420' host='localhost' port='5432'") #psycopg2建立連線
    cur=conn.cursor()                   #建立cursor物件，這樣才可以取得資料庫的資料
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #SOL指令，table名稱為store，欄位名為item(String)，quantity(integer)和price(float)
    conn.commit()  #提交database的改變
    conn.close()   #連線要關閉

def insert(item,quantity,price):
    #conn=psycopg2.connect("lite.db")
    conn = psycopg2.connect("dbname='python_use' user='postgres' password='04500420' host='localhost' port='5432'")
    cur=conn.cursor()
    #cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))   sqlite3用?當作占位符
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))  #psycopg2用%當占位符
    conn.commit()
    conn.close()

def view():
    #conn=psycopg2.connect("lite.db")
    conn = psycopg2.connect("dbname='python_use' user='postgres' password='04500420' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(obj):
    #conn = psycopg2.connect("lite.db")
    conn = psycopg2.connect("dbname='python_use' user='postgres' password='04500420' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("DELETE FROM store WHERE item=?",(obj,))   取代符後面要加逗號，sqlite3
    cur.execute("DELETE FROM store WHERE item=%s", (obj,))  #psycopg2用法
    conn.commit()
    conn.close()

def update(quantity,price,item):
    #conn = psycopg2.connect("lite.db")
    conn = psycopg2.connect("dbname='python_use' user='postgres' password='04500420' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))  
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()

create_table()
#insert("orange",11,4)
#delete("orange")
update(15,5,"apple")
print(view())
