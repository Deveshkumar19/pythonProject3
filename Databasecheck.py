import mysql.connector


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "London@99")

#printing the connection object
print(myconn)