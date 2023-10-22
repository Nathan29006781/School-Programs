#Friday, Nov 26, 2021
#A database to store, retrieve, and modify student info. Now incorporates SQL
#By: Nathan and Will
#Class: ICS3U0 - Mr. Tombs

import functions as f
import studentFunctions as s
import classFunctions as c
import Globals as g
import sql #our file
from time import sleep
from os import system

#Opens the sql database
if sql.start_up():
  #Saves sql data to python lists
  g.students = sql.to_list(sql.students)
  g.classes = sql.to_list(sql.classes)
else:
  print("SQL ERROR UPON STARTING UP")
  sleep(7)

system('clear')

#Intro message 
print(f"""{g.blue}
_____________________________________________{g.yellow}
|                                           |
|   Welcome to the PCSS Student Database!   |
|{g.blue}___________________________________________{g.yellow}|
""")

#Gives user options for program
f.listRun("What would you like to do?", ["Students", "Classes"], [s.studentInfo, c.classInfo,]) #Runs the menu with the list of options

exit = f.listReturn("How would you like to Exit?", ["not Save and Exit", "Save and Exit"])

if exit:
  try:
    sqliteConnection, cursor = sql.get_connection() #Connects to SQL

    sql.delete_table(sql.students, cursor, sqliteConnection) #Deletes the two pre-existing sql tables
    sql.delete_table(sql.classes, cursor, sqliteConnection)
    sql.save_data(sql.students, g.students, cursor, sqliteConnection)
    #Saves the new, updated data by creating new tables
    sql.save_data(sql.classes, g.classes, cursor, sqliteConnection)

    #Close the cursor
    cursor.close()
    print(f"{g.green}Saved.") #Confirms it has been saved
  except: #Raises an error message if unable to save
    print(f"{g.red}Error while saving data.", Exception)
  finally: #Closes the SQL connection
    if sql.close_connection(sqliteConnection):
      print("SQLite connection is closed.")

print(f"\n{g.violet}Thanks for visiting! Goodbye. {g.reset}") #Goodbye message