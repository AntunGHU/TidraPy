# 8'46''
# postgres treba instalirati, instalirao iz terma, iz app-a i sa scriptom stranice https://www.postgresql.org/download/linux/ubuntu/
# sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg list'
# wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
# sudo apt-get update
# sudo apt-get -y install postgresql

## probao i sljedecu kdu: " sudo apt-get install postgresql-12 " a poslije sa youtube-videa vidio da treba i "sudo apt-get install postgresql-contrib". Potom prijava u postgres sa "sudo -i -u postgres" pa sa "psql" u postgres=# prompt iz kog izlazim sa \q ali tada vise nisam mogao iz usera postgres. Drugi način direktnog ulaska u postgres prompt je "sudo -u postgres psql" a izlazak iz njega u usera antun isti \q. Promjenio def pass za defusera postgres na 'a6PG'. 
## Tjekom gledanja videa o installu PG i pgAdmin-a instalirao pgAdmin4 i stavio "svoj pass" xxxxxxPG kao master. Kreirao server "AntunPGS", u connection u polje hostname/email stavio "localhost", ime database "postgres", username "postgres", password "a6PG" i Save! Pojavio se sever "AntunPGS" u pgAdmin4!!!  Potom sukladno tjeku videa konfiguriram web pgAdmin4. Stavljam email:"antun@antun.jer", pass: "aaj123", potvrdjujem 2 pitanja sa y i enter (jedno vezano za apache) Dobijam poruku da sad mogu startati pgAdmin4 u web modu ukucavajuci kdnu http://127.0.0.1/pgadmin4 . Probavam i ulazim! Medjutim, sve sto sam u desktop modu konfigao ovdje se ne vidi tako da se mora ispocetka. Konfiguriram jednako kao desktop mod:ime servera "AntunPGS", u connection hostname "localhost", ime database "postgres", ime usera je po defu  "postgres" . Stavljam pass isti kao u Desktop-modu 'a6PG' Takodjer zakacinje checkbox za Save password.


# import psycopg2

#def create_table():
#    conn=sqlite3.connect("lite.db")
#    cur=conn.cursor()
#    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
#    conn.commit()
#    conn.close()
#    
#def insert(item, quantity, price):
#    conn=sqlite3.connect("lite.db")
#    cur=conn.cursor()
#    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
#    conn.commit()
#    conn.close()
#
#def view():
#    conn=sqlite3.connect("lite.db")
#    cur=conn.cursor()
#    cur.execute("SELECT * FROM store")
#    rows=cur.fetchall()     # rows are py-list
#    conn.commit()
#    conn.close()
#    return rows
#
#def delete(item):
#    conn=sqlite3.connect("lite.db")
#    cur=conn.cursor()
#    cur.execute("DELETE FROM store WHERE item=?", (item,))
#    conn.commit()
#    conn.close()
#    
#def update(quantity,price,item):
#    conn=sqlite3.connect("lite.db")
#    cur=conn.cursor()
#    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
#    conn.commit()
#    conn.close()
#
#
## insert("Kecap", 5, 10.2) 
## delete("Kecap")
#update(100,101,"Vino")
#print(view())