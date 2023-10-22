#Monday, Nov 8, 2021
#A database to store, retrieve, and modify student info
#By: Nathan and Will
#Class: ICS3U0 - Mr. Tombs

import functions as f
import studentFunctions as s
import Globals as g
import csv


#Opens the student csv file and extracts the data
file = open('students.csv')
fileData = csv.reader(file , delimiter=",")
g.students = list(fileData) #Saves csv file to list
  
print(f"""{g.blue}
_____________________________________________{g.yellow}
|                                           |
|   Welcome to the PCSS Student Database!   |
|{g.blue}___________________________________________{g.yellow}|
""")
f.listRun("Pick an Option",["Add a Student", "Remove a Student", "Modify Student Information", "Look at Student Information"], [s.getInfo, s.deleteInfo, s.modifyInfo, s.displayInfo]) #Runs the menu with the list of options

exit = f.listReturn("How would you like to Exit?", ["not Save and Exit", "Save and Exit"]) #Saves the data and updates the csv file if the user wants to

if exit:
  with open('students.csv', 'w') as f: #Opens a csv writer to update the info
    write = csv.writer(f)
    for student in g.students: #Saves data back to file row by row
      write.writerow(student)
  print(f"{g.green}Saved.") #Confirms it has been saved

print(f"\n{g.violet}Thanks for visiting! Goodbye. {g.reset}") #Goodbye message