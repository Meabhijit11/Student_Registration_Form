import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="regi_form"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE form_data (Fname VARCHAR(255), Lname VARCHAR(255), Day INT(10), Month VARCHAR(255), Year INT(10), Email VARCHAR(255), Mobile VARCHAR(255), Gender VARCHAR(255), Address VARCHAR(255), City VARCHAR(255), Pin VARCHAR(255), State VARCHAR(255), Country VARCHAR(255), Hobby VARCHAR(255), Class_X_Board VARCHAR(255), Class_X_Percentage VARCHAR(255), Class_X_Year_Of_Passing VARCHAR(255), Class_XII_Board VARCHAR(255), Class_XII_Percentage VARCHAR(255), Class_XII_Year_Of_Passing VARCHAR(255) , Diploma_Board VARCHAR(255), Diploma_Percentage VARCHAR(255), Diploma_Year_Of_Passing VARCHAR(255) , Degree_Board VARCHAR(255), Degree_Percentage VARCHAR(255), Degree_Year_Of_Passing VARCHAR(255) , Cource_Applied VARCHAR(255))")

mycursor = mydb.cursor()
