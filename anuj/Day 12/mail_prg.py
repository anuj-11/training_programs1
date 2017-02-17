import MySQLdb
db = MySQLdb.connect("localhost","root","root","maildb")
cursor = db.cursor()
#cursor.execute("DROP TABLE IF EXISTS sometable")
#cursor.execute("""CREATE TABLE sometable(FIRST_NAME VARCHAR(20),LAST_NAME VARCHAR(20),AGE INT)""")
#try:
cursor.execute("INSERT INTO sometb(Name,Job,Age) VALUES('Anuj','SE',24)")
cursor.execute("INSERT INTO sometb(Name,Job,Age) VALUES('Dexter','BSA',34)")
sql = """SELECT DISTINCT Name FROM sometb"""
with open("names.txt", "w") as file1:
	cursor.execute(sql)
#rows=cursor.fetchall()
	for row in cursor:
		print>>file1, row[0]
db.commit()
#except:
#	db.rollback()
db.close()
