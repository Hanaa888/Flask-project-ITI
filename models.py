import sqlite3


DATABASE = "patients.db"
conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

cursor.execute("""
update Userinfo set name = "AA 1" where ID=4
 """) 

conn.commit()
conn.close()

print("Done.")
