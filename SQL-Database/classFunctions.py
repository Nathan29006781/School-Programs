import functions as f
import Globals as g
import classFunctions as s

#We added an extra s on the end of class because class is reserved

noClass = f"{g.red}Class not found."

def fixClassInfo(classs):
  #Modifies data
  classs[0] = classs[0].upper() #Class Code
  classs[1] = classs[1].capitalize() #Capitalize
  classs[2] = classs[2].capitalize() #Teacher

  joinDate = list(classs[4]) #Replaces inputed values to fit the (YYYY-MM-DD) format
  joinDate[4] = '-'
  joinDate[7] = '-'
  classs[4] = ''.join(joinDate)

  return classs

def getClassInfo(): #Function to add a new class
  classs = ['','','','','',''] #Gets a blank array for a new class
  for i in range (len(g.classTemplate)):
    print(classs)
    if f.containsOnlyText(g.classTemplate[i]): #Chekcs if the classTemplate is one that contains only text
      classs[i] = f.acquirePureText(g.classPrompts[i]) #Uses the acquire text function that accepts only text
    elif type(g.classTemplate[i]) == type(""):
      classs[i] = f.acquireAlphaText(g.classPrompts[i], g.classTemplate[i]) #Uses the acquire text function that accepts alphanumeric text
    elif type(g.classTemplate[i]) == type((0, 0)): #If it contains a tuple than it accepts only integers
      range_start = int(g.classTemplate[i][0]) #Uses the two numbers in the tuple as a range
      range_end = int(g.classTemplate[i][1])
      classs[i] = f.acquireNum(g.classPrompts[i], True, range_start, range_end)

  classs = fixClassInfo(classs) #Updates the class's information
  g.classes.append(classs) #Adds the updated information to the database
  print(f"{g.green}{classs[0]} has been added:")
  print(classs) #Shows the class file that was updated with fixed changes
  f.back()

def dataToClass(): #Function to locate classs based on user's input/choice. Returns the class if found.
  choice = f.listReturn("How do you want to look for the Class?", g.classPrompts)
  if type(g.classTemplate[choice]) == type(""): #Chekcs if the classTemplate is one that contains only text
    info = f.acquirePureText(g.classPrompts[choice]) #Uses the acquire text function that accepts only text
  elif type(g.classTemplate[choice]) == type(1):
    info = f.acquireAlphaText(g.classPrompts[choice], g.classTemplate[choice]) #Uses the acquire text function that accepts alphanumeric text
  elif type(g.classTemplate[choice]) == type((0, 0)): #If it contains a tuple than it accepts only integers
    range_start = int(g.classTemplate[choice][0]) #Uses the two numbers in the tuple as a range
    range_end = int(g.classTemplate[choice][1])
    info = f.acquireNum(g.classPrompts[choice], True, range_start, range_end)

  matches = [] #List to store classs that matched input
  for classs in g.classes:
    if str(info).capitalize() == str(classs[choice]).capitalize(): #Compares data case insensitively
      matches.append(classs)
  
  if len(matches) == 1:
    print(f"{g.green}A match was found!{g.reset}")
    return matches[0] #Returns the one matched class
  elif len(matches) == 0: #If no direct matches were found
    for classs in g.classes:
      if str(info).lower() in str(classs[choice]).lower(): #Checks for substrings case insensitively
        matches.append(classs)

    if len(matches) == 1:
      print(f"{g.green}No matches were found! 1 indirect match found{g.reset}")
      return matches[0] #Returns the one matched class
    elif len(matches) == 0: return(noClass) #Returns if no matching/similar data was found
    else: print(f"No matches were found for {info}. {len(matches)} other matches were found instead.") #Returns if similar data was found, but not exactly the same
  else: print(f"{len(matches)} matches were found for {info}.") #Returns if the multiple exact matches are found

  Names = [] #Creates list of names of matching classs
  for classs in matches:
    Names.append(classs[0] + " - " + classs[1])
  Names.append(noClass)

  Name = Names[f.listReturn("Select the correct class: ", Names)] #Lists the different options of exact matches so users can select the proper one

  for classs in matches: #Checks which class was chosen
    if Name == classs[0] + " - " + classs[1]: return classs #Returns the correct class
  return Name #Should be class not found

def classMatch(classs): #Dsplays all students in a selected class
  class_matches = []
  class_code = classs[0]
  for student in g.students:
    if class_code == student[6]: class_matches.append(student) 
  
  if class_matches: #Prints the students in the selected class
    for student in class_matches: print(student)
  else: #If the class is empty
    print(f"{g.red}No Students in {class_code}")
  f.back()

def printClass(classs): #Takes in a class and prints the file
  if classs != noClass: #Only works if given a class in the database
    for i in range(len(g.classPrompts)):
      print(f"{g.classPrompts[i]}{classs[i]}") #Prints the class selected
  else: print(classs) #Should be "Class Not Found"
  f.back()

def deleteClass(classs): #Deletes a specific class
  if classs != noClass: #Only works if given a class in the database
    g.classes.remove(classs) #Deletes the class selected
    print(f"{g.red}Deleted {classs[0]} - {classs[1]}")
  else: print(classs) #Should be "Class Not Found"
  f.back()

def deleteAllClasses(): #Deletes all classs from the database
  g.classes.clear()
  print(f"{g.red}Deleted all classes")
  f.back()

def printAllClasses(): #Prints all the classs in the database
  if g.classes:
    for classs in g.classes: print(classs)
  else: #If the database is empty
    print("No Classes in Database")
  f.back()

def deleteClassInfo(): #Deletes the class(es) based on what options the user chooses
  f.listRun("Select the correct class: ", ["Delete all classes", "Delete a class by Lookup"],[deleteAllClasses, lambda: deleteClass(dataToClass())])

def displayClassInfo(): #Displays the class(es) based on what options the user chooses
  f.listRun("Select the correct class: ", ["Display all classes", "Display a class by Lookup", "Display all students in a class"],[printAllClasses, lambda: printClass(dataToClass()), lambda: classMatch(dataToClass())])

def modifyClassInfo(): #Allows the user to change the information on a class file
  classs = dataToClass() #Acquires the selected class's information
  if classs != noClass: #Runs if the class exists in the database
    for i in range (len(g.classTemplate)): #Checks each entry in the classTemplate list
      print(classs)
      if f.containsOnlyText(g.classTemplate[i]): #Chekcs if the classTemplate is one that contains only text
        info = f.acquirePureText(g.classPrompts[i] + classs[i] + "\nNew " + g.classPrompts[i]) #Uses the acquire text function that accepts only text
      elif type(g.classTemplate[i]) == type(""):
        info = f.acquireAlphaText(g.classPrompts[i] + str(classs[i]) + "\nNew " + g.classPrompts[i], g.classTemplate[i]) #Uses the acquire text function that accepts alphanumeric text
      elif type(g.classTemplate[i]) == type((0, 0)): #If it contains a tuple than it accepts only integers
        range_start = int(g.classTemplate[i][0]) #Uses the two numbers in the tuple as a range
        range_end = int(g.classTemplate[i][1])
        info = f.acquireNum(g.classPrompts[i] + str(classs[i]) + "\nNew " + g.classPrompts[i], True, range_start, range_end)
      
      if info != "": classs[i] = info #Saves new info
  #'class[i] = info' works because python lists are mutable. Meaning it modifies the original class file
    classs = fixClassInfo(classs)
  print(classs) #Prints the updated info
  f.back()

def classInfo():
  f.listRun("Pick an Option",["Add a Class", "Remove a Class", "Modify Class Information", "Look at Class Information"], [getClassInfo, deleteClassInfo, modifyClassInfo, displayClassInfo]) #Runs the classes menu with the list of options
