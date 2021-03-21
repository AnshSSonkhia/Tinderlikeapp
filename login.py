import mysql.connector

conn=mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tinder")

mycursor=conn.cursor()

#mycursor.execute("CREATE DATABASE tinder")
#conn.commit()

#mycursor.execute("CREATE TABLE proposals (proposal_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, romeo INT NOT NULL,juliet INT NOT NULL)")

#conn.commit()

mycursor.execute("INSERT INTO users(user_id, name, email, password) VALUES(NULL, 'Mithali palkar', 'mithali@thgmail.com', '1010')")
conn.commit()

#mycursor.execute("SELECT * FROM users WHERE name LIKE 'r%' ")
#data=mycursor.fetchall()
#for i in data:
   # print(i[2],i[1])

#mycursor.execute("UPDATE users SET password='2001' WHERE user_id=1")
#conn.commit()

#mycursor.execute("DELETE FROM users WHERE user_id=2")
#conn.commit()



