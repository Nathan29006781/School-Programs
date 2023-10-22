#Import functions from other files
import functions as f
import Globals as g

noStudent = f"{g.red}Student not found."

#Takes in a student and "sanitizes" the data. returns reformatted data
def fixStudentInfo(student):
  #Modifies data
  student[1] = student[1].capitalize() #First Name
  student[2] = student[2].capitalize() #Last Name

  gender = student[4] #Gender
  student[4] = ""
  for word in gender.split(): student[4] = ''.join([student[4], word[0].upper()])

  if student[3] == "" and student[5] != "": student[3] = student[5]+5 #Guesses the age/grade if other info given
  if student[5] == "" and student[3] != "": student[5] = student[3]-5

  student[6] = student[6].upper() #Course Code

  return student

def getStudentInfo(): #Function to add a new student
  student = ['','','','','','', ''] #Gets a blank array for a new student
  for i in range (len(g.studentTemplate)):
    if f.containsOnlyText(g.studentTemplate[i]): #Chekcs if the studentTemplate is one that contains only text
      student[i] = f.acquirePureText(g.studentPrompts[i]) #Uses the acquire text function that accepts only text
    elif type(g.studentTemplate[i]) == type(""):
      student[i] = f.acquireAlphaText(g.studentPrompts[i], g.studentTemplate[i]) #Uses the acquire text function that accepts alphanumeric text
    elif type(g.studentTemplate[i]) == type((0, 0)): #If it contains a tuple than it accepts only integers
      range_start = int(g.studentTemplate[i][0]) #Uses the two numbers in the tuple as a range
      range_end = int(g.studentTemplate[i][1])
      student[i] = f.acquireNum(g.studentPrompts[i], True, range_start, range_end)

  student = fixStudentInfo(student) #Updates the student's information
  g.students.append(student) #Adds the updated information to the database
  print(f"{g.green}{student[0]} has been added:")
  print(student) #Shows the student file that was updated with fixed changes
  f.back()

def dataToStudent(): #Function to locate students based on user's input/choice. Returns the student if found.
  choice = f.listReturn("How do you want to look for the Student?", g.studentPrompts)
  if type(g.studentTemplate[choice]) == type(""): #Chekcs if the studentTemplate is one that contains only text
    info = f.acquirePureText(g.studentPrompts[choice]) #Uses the acquire text function that accepts only text
  elif type(g.studentTemplate[choice]) == type(1):
    info = f.acquireAlphaText(g.studentPrompts[choice], g.studentTemplate[choice]) #Uses the acquire text function that accepts alphanumeric text
  elif type(g.studentTemplate[choice]) == type((0, 0)): #If it contains a tuple than it accepts only integers
    range_start = int(g.studentTemplate[choice][0]) #Uses the two numbers in the tuple as a range
    range_end = int(g.studentTemplate[choice][1])
    info = f.acquireNum(g.studentPrompts[choice], True, range_start, range_end)

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
    elif len(matches) == 0: return(noStudent) #Returns if no matching/similar data was found
    else: print(f"No matches were found for {info}. {len(matches)} other matches were found instead.") #Returns if similar data was found, but not exactly the same
  else: print(f"{len(matches)} matches were found for {info}.") #Returns if the multiple exact matches are found

  Names = [] #Creates list of names of matching students
  for student in matches:
    Names.append(student[1] + " " + student[2])
  Names.append(noStudent)

  Name = Names[f.listReturn("Select the correct student: ", Names)] #Lists the different options of exact matches so users can select the proper one

  for student in matches: #Checks which student was chosen
    if Name == student[1] + " " + student[2]: return student #Returns the correct student
  return Name #Should be student not found

def numToStudent(): #Function that finds a student based on which row of the data base they are
  return g.students[f.acquireNum("Student's Entry Number: ", False, 0, len(g.students)) - 1] #Returns the student corresponding to the number picked

def printStudent(student): #Takes in a student and prints the file
  if student != noStudent: #Only works if given a student in the database
    for i in range(len(g.studentPrompts)):
      print(f"{g.studentPrompts[i]}{student[i]}") #Prints the student selected
  else: print(student) #Should be "Student Not Found"
  f.back()

def deleteStudent(student): #Deletes a specific student
  if student != noStudent: #Only works if given a student in the database
    g.students.remove(student) #Deletes the student selected
    print(f"{g.red}Deleted {student[1]} {student[2]}")
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

def deleteStudentInfo(): #Deletes the student(s) based on what options the user chooses
  f.listRun("Select the correct student: ", ["Delete all students", "Delete a student by Entry Number", "Delete a student by Lookup"],[deleteAllStudents, lambda: deleteStudent(numToStudent()), lambda: deleteStudent(dataToStudent())])

def displayStudentInfo(): #Displays the student(s) based on what the options the user chooses
  f.listRun("Select the correct student: ", ["Look at all students", "Pick a student by Entry Number", "Pick a student by Lookup"],[printAllStudents, lambda: printStudent(numToStudent()), lambda: printStudent(dataToStudent())])

def modifyStudentInfo(): #Allows the user to change the information on a student file
  student = dataToStudent() #Acquires the selected student's information
  if student != noStudent: #Runs if the student exists in the database
    for i in range (len(g.studentTemplate)): #Checks each entry in the studentTemplate list
      print(student)
      if f.containsOnlyText(g.studentTemplate[i]): #Chekcs if the studentTemplate is one that contains only text
        info = f.acquirePureText(g.studentPrompts[i] + student[i] + "\nNew " + g.studentPrompts[i]) #Uses the acquire text function that accepts only text
      elif type(g.studentTemplate[i]) == type(""):
        info = f.acquireAlphaText(g.studentPrompts[i] + str(student[i]) + "\nNew " + g.studentPrompts[i], g.studentTemplate[i]) #Uses the acquire text function that accepts alphanumeric text
      elif type(g.studentTemplate[i]) == type((0, 0)): #If it contains a tuple than it accepts only integers
        range_start = int(g.studentTemplate[i][0]) #Uses the two numbers in the tuple as a range
        range_end = int(g.studentTemplate[i][1])
        info = f.acquireNum(g.studentPrompts[i] + str(student[i]) + "\nNew " + g.studentPrompts[i], True, range_start, range_end)
      
      if info != "": student[i] = info #Saves new info
  #'student[i] = info' works because python lists are mutable. Meaning it modifies the original student file
    student = fixStudentInfo(student)
  print(student) #Prints the updated info
  f.back()

def studentInfo():
  f.listRun("Pick an Option",["Add a Student", "Remove a Student", "Modify Student Information", "Look at Student Information"], [getStudentInfo, deleteStudentInfo, modifyStudentInfo, displayStudentInfo]) #Runs the student menu with the list of options