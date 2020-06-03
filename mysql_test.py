import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", 
								passwd="secretsecret",database="learn_python",
								auth_plugin="mysql_native_password")

mycursor = mydb.cursor()

mycursor.execute("select * from marks")

rows =[]
for row in mycursor:
	print(row)
	rows.append(row)

print(rows[2])