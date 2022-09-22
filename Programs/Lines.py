#Nathan Menezes
#Date: Sep 15, 2021
#Purpose: To analyze a line, given 2 coordinate

########################################################
#                     Variables                        #
# Variables that start with 'f' are the alternate      #
# counterparts to the normal vars (usually fractions)  #
#                                                      #
# eq = equation                                        #
# m = slope                                            #
# b = y-intercept                                      #
# a = x-intercept                                      #
# dx or dy = delta ...                                 #
# sx or sy = sum ...                                   #
#                                                      #
########################################################

from os import system #for clearing screen
import sys #For ending program


import math
from fractions import Fraction

def isfloat(text): #Checks if float given string
  try:
    float(text)
    return True
  except ValueError:
    return False

def possible_int (num): #Only give this floats, checks if number can be cast to int and then does it
  if num.is_integer(): num = int(num)
  return num

def checkNum(prompt, range_start="", range_end=""): #Checks if input is a number and within an optional range. Also formats as int if it is an int. Waits until valid input
  val = input(prompt + "\033[0m")
  while True:
    system('clear')
    if isfloat(val): #Checks if it is a number
      val = float(val)
      val = possible_int(val)
      if range_start != "" and range_end != "": #If a range was given
        if val in range(range_start, range_end+1): return val #If in the range
      else: return val
    print("\033[31mNot a valid entry. Try again\033[0m\n")
    val = input(prompt + "\033[0m")

x1 = checkNum("\033[92mPlease enter x1: ")
y1 = checkNum("\033[92mPlease enter y1: ")
x2 = checkNum("\033[92mPlease enter x2: ")
y2 = checkNum("\033[92mPlease enter y2: ")

#Math to get equations
dx = x2-x1 #delta x for simpler calculations
dy = y2-y1
sx = x2+x1  #Sums the x values to be used in average for midpoint later
sy = y2+y1

sx = possible_int(sx/2.0) #Ternary that halves and casts to int if possible
sy = possible_int(sy/2.0)
fsx = Fraction(sx).limit_denominator(100000)  #Prevents weird fractions caused by floating point errors
fsy = Fraction(sy).limit_denominator(100000)

if dy != 0 and dx != 0: #If normal line (slope is not undef or 0)
    m = dy/dx #Slope
    b = y1-m*x1 #Y-Intercept
    a = -b/m #X-intercept

    m = possible_int(m) #Casts to int if possible
    b = possible_int(b)
    a = possible_int(a)

    fm = Fraction(m).limit_denominator(100000) #Creates fraction forms and prevents weird ones caused by floating point errors
    fb = Fraction(b).limit_denominator(100000)
    fa = Fraction(a).limit_denominator(100000)

    #This section looks messy because I am using actual vars to hold temp vals
    d = pow(dy, 2) + pow(dx, 2) # temporarily saves (y2-y1)^2 + (x2-x1)^2
    fd = round(math.sqrt(d), 6) #Saves the distance as a decimal
    fd = possible_int(fd) #Deletes trailing zeros if possible
    if isinstance(dy, int) and isinstance(dx, int) and not isinstance(fd, int): fd = f"√{d}" #uses root symbol if the radicand will be an int
    d = round(math.sqrt(d), 6) #Saves the distance as a decimal

    fang = math.atan(m)
    ang = round(math.degrees(fang), 6) #Saves the angle in deg with respect to the x-axis
    if ang < 0: ang += 180 #negative angles are corrected to the positive equivalent
    ang = possible_int(ang)
    fang = round(fang, 6)

    if (isinstance(possible_int(ang/11.25), int)): #Writes angle as multiple of pi in rads if possible
      fang = Fraction(possible_int(ang/11.25)/16)
      if(fang.numerator == 1): fang = "π/" + str(fang.denominator)
      else: fang = f"{fang.numerator}π/{fang.denominator}"


    if m == 1: eq = feq = "y = x" #slope of 1
    elif m == -1: eq = feq = "y = -x" #slope of -1
    else:
      eq = f"y = {m}x"
      feq = f"y = {fm}x"

    if b>0: #positive y-intercept
      eq = eq + f" + {b}"
      feq = feq + f" + {fb}"
    elif b<0: #negative y-intercept
      eq = eq + f" - {-b}"
      feq = feq + f" - {-fb}"
else:
  if dx == 0 and dy == 0: #Same Point
    eq = "Same Point"
    m = b = a = ang = fang ="Undefined"
    d = 0
  elif dx == 0: #Vertical line
    eq = f"x = {x1}"
    m = b = "Undefined"
    a = x1
    d = abs(dy)
    ang = 90
    fang = "π/2"
  elif dy == 0: #Horizontal line
    eq = f"y = {y1}"
    m = 0
    b = y1
    a = "Undefined"
    d = abs(dx)
    ang = fang = 0 
  feq = eq #In abnormal lines (slope is undef or 0), the fraction forms are equivalent to the decimal
  fm = m
  fb = b
  fa = a
  fd = d

#Asking what to display
view = 1
while True: #Checks for valid view choice
  choice = checkNum("""\033[92m
  Press 1 for Equation
  Press 2 for Slope
  Press 3 for Y-Intercept
  Press 4 for X-Intercept
  Press 5 for Distance
  Press 6 for Midpoint
  Press 7 for Angle
  Press 8 for All
  """, 1, 8)

  while True: #Allows multiple view selctions
    print(f"\n\033[95m({x1}, {y1}), ({x2}, {y2})")
    if view == 1:
      if choice == 1: print (f"\033[92mEquation: \033[0m{eq}")
      elif choice == 2: print (f"\033[92mSlope: \033[0m{m}")
      elif choice == 3: print (f"\033[92mY-intercept: \033[0m{b}")
      elif choice == 4: print (f"\033[92mX-intercept: \033[0m{a}")
      elif choice == 5: print (f"\033[92mDistance: \033[0m{d}")
      elif choice == 6: print (f"\033[92mMidpoint: \033[0m({sx}, {sy})")
      elif choice == 7: print (f"\033[92mAngle: \033[0m{ang} deg")
      elif choice == 8:
        print (f"\033[92mEquation:\033[0m  {eq}")
        print (f"\033[92mSlope:\033[0m         {m}")
        print (f"\033[92mY-intercept:\033[0m   {b}")
        print (f"\033[92mX-intercept:\033[0m   {a}")
        print (f"\033[92mDistance:\033[0m      {d}")
        print (f"\033[92mMidpoint:\033[0m      ({sx}, {sy})")
        print (f"\033[92mAngle:\033[0m         {ang} deg")
    
    else:
      if choice == 1: print (f"\033[92mEquation: \033[0m{feq}")
      elif choice == 2: print (f"\033[92mSlope: \033[0m{fm}")
      elif choice == 3: print (f"\033[92mY-intercept: \033[0m{fb}")
      elif choice == 4: print (f"\033[92mX-intercept: \033[0m{fa}")
      elif choice == 5: print (f"\033[92mDistance: \033[0m{d}")
      elif choice == 6: print (f"\033[92mMidpoint: \033[0m({fsx}, {fsy})")
      elif choice == 7: print (f"\033[92mAngle: \033[0m{ang} deg")
      elif choice == 8:
        print (f"\033[92mEquation:\033[0m  {feq}")
        print (f"\033[92mSlope:\033[0m         {fm}")
        print (f"\033[92mY-intercept:\033[0m   {fb}")
        print (f"\033[92mX-intercept:\033[0m   {fa}")
        print (f"\033[92mDistance:\033[0m      {fd}")
        print (f"\033[92mMidpoint:\033[0m      ({fsx}, {fsy})")
        print (f"\033[92mAngle:\033[0m         {fang} rad")

    end = checkNum("\033[4m\nWould you like to do something else?\033[0m\033[94m\n1 for Alternate view\n2 for Choose another option\n3 for End program\n\033[0m", 1, 3) #Options to end program or return to selction menu
    if end == 1: view = 1-view
    elif end == 2: break
    elif end == 3: sys.exit('\033[95mGoodbye!')