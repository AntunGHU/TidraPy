# 24'28''
# Ataciranje funkcija button-ima
# to mozemo i unutar frontend scripte ali Ard vise voli to kroz posebnu "backend.py" scriptu koju ce potom importati u frontend.
# za mene ce to u konacnici znaciti pravljenje kopija mojih fajlova jer pocinju sa brojevima. Samo cu izbaciti brojeve! u kopijama fajlova

import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
# insert("Maca", "Anja jerak Glavan", 1963, 975436464)
# insert("Maca", "Antun Jerak", 1963, 975436464)
# delete(1)
# update(3,"Macaaa", "Anjaaa", 1991, 99555555)
# print(view())
# print(search(author="Antun Jerak"))

