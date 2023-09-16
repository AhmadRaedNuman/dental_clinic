import mysql.connector
DentalClinic = mysql.connector.connect(
    host="localhost", user='root', password='', database='dental clinic')
cursor = DentalClinic.cursor()
