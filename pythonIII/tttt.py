import sqlite3

conn = sqlite3.connect('mojadb.db')
c = conn.cursor()


# c.execute('Delete from oddelenie')
# c.execute('delete from zamestnanec')


#c.execute("insert into zamestnanec values (6,'Vlado',9,2000)");
c.execute('insert into oddelenie values(4,"Accounting")')


conn.commit()