import sqlite3

conn = sqlite3.connect("mojadb.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users 
                        (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL
                        )
""")

# cur.execute("insert into users (username,password) values (?,?)",("admin","silneheslo"))
# conn.commit()

username = input("Zadaj username: ")
password = input("Zadaj heslo: ")

#cur.execute(f"select * from users where username='{username}' and password='{password}'")
#cur.execute(f"select * from users where username='"+username+"' and password='"+password+"'")
cur.execute("select * from users where username=? and password=?",(username,password))

"select * from users where username='' or 1=1 --"
data = cur.fetchone()

if data:
    print("pripojeny")
else:
    print("Zadal si zle meno alebo heslo")


conn.commit()



cur.close()
conn.close()