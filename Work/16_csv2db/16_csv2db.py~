#Jiajie Mai
#SoftDev1 pd7
#K16 No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#peeps.csv
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER"
#build SQL stmt, save as string
c.execute(command)    #run SQL statement

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = ""
        command += "INSERT INTO peeps VALUES ("
        command += "'" + row['name'] + "', "
        command += row['age'] + ", "
        command +=  row['id'] + ")"
        c.execute(command)
        
#courses.csv
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER"
c.execute(command)

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = ""
	command += "INSERT INTO courses VALUES ("
	command += "'" + row['name'] + "', "
	command += row['age'] + ", "
	command +=  row['id'] + ")"
        c.execute(command)

        

#==========================================================

db.commit() #save changes
db.close()  #close database
