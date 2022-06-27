# 12'51''
# 6'54''
# brisanje i promjene. psycopg2 stalno odbijao da se instalira i importa dok nisam naisao na k-du "sudo apt-get install python3-psycopg2"!!!

import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='postgres' user='postgres' password='a6PG' host='localhost' port='5432' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='postgres' user='postgres' password='a6PG' host='localhost' port='5432' port='5432'")
    cur=conn.cursor()
    # cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    # cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price)) # opcija osjetljiva na SQL injections
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)" , (item, quantity, price)) # popravak osjetljivosti
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='postgres' user='postgres' password='a6PG' host='localhost' port='5432' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()     # rows are py-list
    conn.commit()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='postgres' user='postgres' password='a6PG' host='localhost' port='5432' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()
    
def update(quantity,price,item):
    conn=psycopg2.connect("dbname='postgres' user='postgres' password='a6PG' host='localhost' port='5432' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()

create_table()
# insert("Orang", 15, 10)
insert("Kecap", 5, 10.2) 
delete("Aplle") # obrisao sve unose, bilo ih 3!!!
update(100,101,"Orang")
print(view())
