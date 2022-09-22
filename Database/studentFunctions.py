#Import functions from other files
import functions as f
import Globals as g

#Takes in a student and "sanitizes" the data. returns fixed data
def fixInfo(student):
  #Modifies data
  student[0] = student[0].capitalize() #First Name
  student[1] = student[1].capitalize() #Last Name

  gender = student[3] #Gender
  student[3] = ""
  for word in gender.split(): student[3] = ''.join([student[3], word[0].upper()])

  if student[2] == "" and student[4] != "": student[2] = student[4]+5 #Guesses the age/grade if other info given
  if student[4] == "" and student[2] != "": student[4] = student[2]-5

  return student


def getInfo(): #Function to add a new student
  student = ['','','','','',''] #Gets a blank array for a new student
  for i in range (len(g.template)):
    if f.containsOnlyText(g.template[i]): #Chekcs if the template is one that contains only text
      student[i] = f.acquireText(g.prompts[i], True) #Uses the acquire text function that accepts only text
    else: #If it contains a tuple than it accepts only intergers
      range_start = int(g.template[i][0]) #Uses the two numbers in the tuple as a range
      range_end = int(g.template[i][1])
      student[i] = f.acquireNum(g.prompts[i], True, range_start, range_end)

  student = fixInfo(student) #Updates the student's information
  g.students.append(student) #Adds the updated information to the database
  print(f"{g.green}{student[0]} has been added:")
  print(student) #Shows the student file that was updated with fixed changes
  f.back()


def dataToStudent(): #Function to locate students based on user's input/choice. Returns the student if found.
  choice = f.listReturn("How do you want to look for the Student?", g.prompts)
  if f.containsOnlyText(g.template[choice]): #Checks if the input needs text, and only accepts text if it does
    info = f.acquireText(g.prompts[choice], True)
  else: #Checks if the input requires intergers and only accepts intergers if it does, using the two values provided as a range
    range_start = int(g.template[choice][0])
    range_end = int(g.template[choice][1])
    info = f.acquireNum(g.prompts[choice], True, range_start, range_end)

  matches = [] #List to store students that matched input
  for student in g.students:
    if str(info).capitalize() == str(student[choice]).capitalize(): #Compares data case insensitively
      matches.append(student)
  
  if len(matches) == 1:
    print(f"{g.green}A match was found!{g.reset}")
    return matches[0] #Returns the one matched student
  elif len(matches) == 0: #If no direct matches were found
    for student in g.students:
      if str(info).lower() in str(student[choice]).lower(): #Checks for substrings case insensitively
        matches.append(student)

    if len(matches) == 1:
      print(f"{g.green}No matches were found! 1 indirect match found{g.reset}")
      return matches[0] #Returns the one matched student
    elif len(matches) == 0: return(f"{g.red}Student not found.") #Returns if no matching/similar data was found
    else: print(f"No matches were found for {info}. {len(matches)} other matches were found instead.") #Returns if similar data was found, but not exactly the same
  else: print(f"{len(matches)} matches were found for {info}.") #Returns if the multiple exact matches are found

  Names = [] #Creates list of names of matching students
  for student in matches:
    Names.append(student[0] + " " + student[1])

  Name = Names[f.listReturn("Select the correct student: ", Names)] #Lists the different options of exact matches so users can select the proper one

  for student in matches: #Checks which student was chosen
    if Name == student[0] + " " + student[1]: return student #Returns the correct student

def numToStudent(): #Function that finds a student based on which row of the data base they are
  return g.students[f.acquireNum("Student's Entry Number: ", False, 0, len(g.students)) - 1] #Returns the student corresponding to the number picked

def printStudent(student): #Takes in a student and prints the file
  if student != f"{g.red}Student not found.": #Only works if given a student in the database
    for i in range(len(g.prompts)):
      print(f"{g.prompts[i]}{student[i]}") #Prints the student selected
  else: print(student) #Should be "Student Not Found"
  f.back()

def deleteStudent(student): #Deletes a specific student
  if student != f"{g.red}Student not found.": #Only works if given a student in the database
    g.students.remove(student) #Deletes the student selected
    print(f"{g.red}Deleted {student[0]} {student[1]}")
  else: print(student) #Should be "Student Not Found"
  f.back()

def deleteAllStudents(): #Deletes all students from the database
  g.students.clear()
  print(f"{g.red}Deleted all students")
  f.back()

def printAllStudents(): #Prints all the students in the database
  if g.students:
    for student in g.students: print(student)
  else: #If the database is empty
    print("No Students in Database")
  f.back()

def deleteInfo(): #Deletes the student(s) based on what options the user chooses
  f.listRun("Select the correct student: ", ["Delete all students", "Delete a student by Entry Number", "Delete a student by Lookup"],[deleteAllStudents, lambda: deleteStudent(numToStudent()), lambda: deleteStudent(dataToStudent())])

def displayInfo(): #Displays the student(s) based on what the options the user chooses
  f.listRun("Select the correct student: ", ["Look at all students", "Pick a student by Entry Number", "Pick a student by Lookup"],[printAllStudents, lambda: printStudent(numToStudent()), lambda: printStudent(dataToStudent())])

def modifyInfo(): #Allows the user to change the information on a student file
  student = dataToStudent() #Acquires the selected student's information
  if student != f"{g.red}Student not found.": #Runs if the student exists in the database
    for i in range (len(g.template)): #Checks each entry in the template list
      print(student)
      if f.containsOnlyText(g.template[i]): #Text info
        info = f.acquireText(g.prompts[i] + student[i] + "\nNew " + g.prompts[i], True)
      else: #Number info
        range_start = int(g.template[i][0])
        range_end = int(g.template[i][1])
        info = f.acquireNum(g.prompts[i] + str(student[i]) + "\nNew " + g.prompts[i], True, range_start, range_end)

      if info != "": student[i] = info #Saves new info
  #'student[i] = info' works because python lists are mutable. Meaning it modifies the original student file
    student = fixInfo(student)
  print(student) #Prints the updated info
  f.back()