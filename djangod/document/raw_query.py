# <!-- # To find data from another database using raw query

# >>> from django.db import connection
# >>> cursor = connection.cursor()
# >>> cursor.execute('''SELECT count(*) FROM people_person''')
# 1L
# >>> row = cursor.fetchone()
# >>> print row
# (12L,)
# >>> Person.objects.all().count()
# 12




# import mysql.connector  
# #Create the connection object   
# myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "google", database = "mydb")  
  
# #printing the connection object   
# print(myconn)   
  
# #creating the cursor object  
# cur = myconn.cursor()  
  
# print(cur)  -->



# import psycopg2


# def connection():
#     # establishing the connection
#     conn = psycopg2.connect(
#         database="resourcekit_prod", user='dilip', password='IeCaiKu6edet6ue7',
#         host='resourcekit-production.cpvyjwogfdwh.us-east-2.rds.amazonaws.com', port='5432'
#     )

#     # Setting auto commit false
#     conn.autocommit = True

#     # Creating a cursor object using the cursor() method
#     cursor = conn.cursor()
#     return cursor


# def resource_data():
#     # Retrieving data
#     cursor = connection()
#     cursor.execute('''SELECT * from resource''')

#     result = cursor.fetchone()
#     print(result)