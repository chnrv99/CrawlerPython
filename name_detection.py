import sqlite3
con = sqlite3.connect("Classification.db")


cur = con.cursor()
# cur.execute("CREATE TABLE types(link,classification)")

# t1 = ('')
url = 'test'
classs  = -1

# cur.execute("""
# INSERT INTO types(link, classification)
# VALUES (?,?)
# """, (url, classs))

con.commit ()