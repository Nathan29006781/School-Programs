#Import functions from other files and SQL
import sqlite3
import Globals as g #Don't remove

students = { #Dictionary for student table
  "name": "`Student`",
#Creates the student table with all the different values being stored
  "create_query": """
  CREATE TABLE `Student`
  ( `Student_Number` INT UNSIGNED,
  `Student_First_Name` TEXT NOT NULL,
  `Student_Last_Name` TEXT NOT NULL,
  `Student_Age` INT UNSIGNED,
  `Student_Gender` TEXT,
  `Student_Grade` INT UNSIGNED,
  `Homeroom_Class_Code` TEXT NOT NULL,
  PRIMARY KEY (`Student_Number`))""",
#Checks if the table already exists
  "query_exists": """
  SELECT count(name)
  FROM sqlite_master
  WHERE type='table'
  AND name='Student'""",
#The format for updating/providing any changes to the student table
  "insert_query": """
  REPLACE INTO `Student` 
  (`Student_Number`, `Student_First_Name`, `Student_Last_Name`, `Student_Age`, `Student_Gender`, `Student_Grade`, `Homeroom_Class_Code`)
  VALUES (?, ?, ?, ?, ?, ?, ?)""",
#Allows to select a certain thing from students
  "select_query": "SELECT * from `Student`",
#Allows for the deletion of the student table
  "delete": "DROP TABLE `Student`"
}

classes = { #Dictionary for the classes table
  "name": "`Classes`",
#Creates the classes table and details the different values being stored
  "create_query": """
  CREATE TABLE `Classes`
  ( `Class_Code` TEXT NOT NULL, 
  `Class_Subject` TEXT NOT NULL,
  `Teacher_Name` TEXT NOT NULL, 
  `Class_Size` INT NOT NULL, 
  `Start_Date` DATE NOT NULL,
  `Class_Grade_Level` INT NOT NULL, 
  PRIMARY KEY (`Class_Code`))""",
#Checks if the table already exists
  "query_exists": """
  SELECT count(name)
  FROM sqlite_master
  WHERE type='table'
  AND name='Classes'""",
#Allows for the table to be updated
  "insert_query": """
  REPLACE INTO `Classes` 
  ( `Class_Code`, `Class_Subject`, `Teacher_Name`, `Class_Size`, `Start_Date`, Class_Grade_Level) 
  VALUES (?, ?, ?, ?, ?, ?)""",
#Allows for certain values to be selected
  "select_query": "SELECT * from `Classes`",
#Allows for the table to be deleted
  "delete": "DROP TABLE `Classes`"
}

#Function to connect to SQL
def get_connection():
  connection = sqlite3.connect('school_db') #Connects to the school_db file
  return connection, connection.cursor()

#Function to close the SQL connection
def close_connection(connection):
  if connection:
    connection.close() #Closes the connection
    return True
  return False

#Function that loads the pre-existing data into the SQL file (only used once)
def preload_data(data, preload_list, cursor, connection):
  #get the count of tables with the name data
  cursor.execute(data["query_exists"])

  #if the count is 1, then the table exists
  if cursor.fetchone()[0] != 1:
    cursor.execute(data["create_query"])
    connection.commit()
    print("SQLite table created")

  #load the data table with the default data
  cursor.executemany(data["insert_query"], preload_list)
  connection.commit() 
  print(cursor.rowcount, f"Records inserted successfully into {data['name']} table")

#Function to save the data in the python lists to the SQL file
def save_data(data, list_with_data, cursor, connection):
  #recreate tables
  cursor.execute(data["query_exists"])
  if cursor.fetchone()[0] != 1: #If it doesn't exist
    cursor.execute(data["create_query"]) #Creates a new table
    connection.commit()

  #save the list to the database
  cursor.executemany(data["insert_query"], list_with_data) #Inserts the data into a specific table
  connection.commit()
  print(cursor.rowcount, f"Records inserted successfully into {data['name']} table") #Confirmation message

#Function to delete the tables
def delete_table(data, cursor, connection):
  cursor.execute(data["query_exists"]) #Checks if the tables exist
  if cursor.fetchone()[0] == 1: #If it exists
    cursor.execute(data["delete"]) #Deletes the tables
    connection.commit()

#Function to extract data from the SQL file into the python lists
def to_list(sql_data):
  print("\nSaving data to py:")
  try:
    sqliteConnection, cursor = get_connection() #Connects to SQL
    cursor.execute(sql_data["select_query"], ())#Fetches all the data
    records = list(cursor.fetchall()) #Inserts the data into records
    print(f"Total rows are: {len(records)}\n")
    close_connection(sqliteConnection) #Closes connection
    return list(map(lambda info: list(info), records)) #Converts the list of tuples into a list of lists
  except (Exception, sqlite3.Error) as error: #Error message
    print("Error while getting data.", error)

#Function to load up the SQL system
def start_up():
  successful = False
  try:
    sqliteConnection, cursor = get_connection() #Connects to SQL
    print("Successfully Connected to SQLite\n")

  #Only run when getting data for first time after deleting db
    # preload_data(students, g.preload_students, cursor, sqliteConnection)
    # preload_data(classes, g.preload_classes, cursor, sqliteConnection)

    #Close the cursor
    cursor.close()

  except sqlite3.Error as error: #Error message
    print("Error while running SQLite script.", error)
  finally:
    if close_connection(sqliteConnection): #Closes the connection
      print("SQLite connection is closed.") 
      successful = True #Exits the loop
  
  return successful 