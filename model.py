import mysql.connector

def db_init(hostname,username,pw):
	mydb = mysql.connector.connect(
		host=hostname,
		user=username,
		password=pw
	  )
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE IF NOT EXISTS lift_db")


def create_tbl(host,user,pw,db):
	mydb = mysql.connector.connect(host=host,user=user,password=pw,database=db)
	mycursor = mydb.cursor()
	mycursor.execute('''CREATE TABLE IF NOT EXISTS users (id varchar(20) PRIMARY KEY,name VARCHAR(255),floor INT(100),type varchar(255))''')
	mycursor.close()
	mydb.close()

def add_user(host,user,pw,db,details):
	mydb = mysql.connector.connect(host=host,user=user,password=pw,database=db)
	mycursor = mydb.cursor()
	mycursor.execute('''INSERT INTO users (id,name,floor,type) VALUES (%s,%s,%s,%s)''', details)
	mydb.commit()
	mycursor.close()
	mydb.close()

def read_tbl(host,user,pw,db,id):
	mydb = mysql.connector.connect(host=host,user=user,password=pw,database=db)
	mycursor = mydb.cursor()
	mycursor.execute('''SELECT * FROM users WHERE ID LIKE {0}'''.format(id))
	result = mycursor.fetchall()
	mycursor.close()
	mydb.close()
	return result

def del_user(host,user,pw,db,floor_tup):
	mydb = mysql.connector.connect(host=host,user=user,password=pw,database=db)
	mycursor = mydb.cursor()
	mycursor.execute('''DELETE FROM users WHERE floor = %s''',floor_tup)
	mydb.commit()
	mycursor.close()
	mydb.close()


def first_user(host,user,pw,db):
	mydb = mysql.connector.connect(host=host, user=user, password=pw, database=db)
	mycursor = mydb.cursor()
	mycursor.execute('''SELECT * FROM users''')
	result = mycursor.fetchall()
	mycursor.close()
	mydb.close()
	if result:
		return False
	else:
		return True


hostname = "127.0.0.1"
username = "lift_admin"
pw = "tdr16705"
db = "lift_db"
db_init(hostname,username,pw)
create_tbl(hostname,username,pw,db)
#add_user("127.0.0.1","lift_admin","tdr16705","lift_db",("98435984","hari",5,"admin"))
# print(read_tbl("127.0.0.1","lift_admin","tdr16705","lift_db","98435984"))
# print(read_tbl("127.0.0.1","lift_admin","tdr16705","lift_db","98435985"))
# del_user("127.0.0.1","lift_admin","tdr16705","lift_db",("5",))
# print(read_tbl("127.0.0.1","lift_admin","tdr16705","lift_db"))
