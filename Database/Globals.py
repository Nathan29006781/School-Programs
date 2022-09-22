#Colors
darkcyan = '\033[36m'
black  = '\033[30;47m'
red    = '\033[31m'
green  = '\033[32m'
yellow = '\033[33m'
blue   = '\033[34m'
violet = '\033[35m'
beige  = '\033[36m'
white  = '\033[37m'
brown  = '\033[91m'
reset  = '\033[0m'
underline = '\033[4m'

#Default Lists
template = ["", "", (5,100), "", (1,12), (111111,999999)] #What type of data is being asked
prompts = ["Name: ", "Last Name: ", "Age: ", "Gender: ", "Grade: ", "Student Number: "] #Prompts for adding a new student/modifying an existing student
students = [] #Gets student data from csv