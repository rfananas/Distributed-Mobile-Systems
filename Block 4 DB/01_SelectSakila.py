import mysql.connector  # mysql-connector-python not default mässiger one

print("Connecting to sakila....", end="", flush=True)
mydb = mysql.connector.connect(
  host        = "localhost",
  user        = "root",
  passwd      = "admin",
  database    = "sakila",
  auth_plugin = 'mysql_native_password'
)
print("completed!")

stm_selectCities = """ #drei parentheses is ein multiline string
    SELECT
       city_id    AS ID,
       city       AS Name,
       country_id AS Country
    FROM 
       city
    WHERE 
       city like 'O%'
"""

mycursor = mydb.cursor()
mycursor.execute(stm_selectCities)
myresult = mycursor.fetchall()
print(myresult)

print("+------+--------------------------------+------------+")
print("| Id   | City                           | Country ID |")
print("+------+--------------------------------+------------+")
for aRec in myresult:
    print("| {plh:4d} |".format(plh=aRec[0]), end="")
    print(" {plh:30s} |".format(plh=aRec[1]), end="")
    print(" {plh:10d} |".format(plh=aRec[2]), end="")
    print()
    print("+------+--------------------------------+------------+")
print("Records found:", len(myresult), myresult)