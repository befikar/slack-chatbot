import mysql.connector
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="chatbot"
  )
db_cursor = db_connection.cursor()
#Here creating database table as student'
db_cursor.execute("CREATE TABLE chat_msgs (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), message TEXT, created_at DATETIME(6))")
#Get database table'
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
