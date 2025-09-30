# Import the Time module
import time

# Defining the grading terms
def gpa_determine(score):
 if score >= 70:
  return 5.0
 elif score >= 60:
  return 4.0
 elif score >= 50:
  return 3.0
 elif score >= 45:
  return 2.0
 elif score >= 40:
  return 1.0
 else:
  return 0.0
  
# Defining the class
def class_grade(cgpa):
 if cgpa >= 4.5:
  print(f"{name} is on First class")
 elif cgpa >= 3.5:
  print(f"{name} is on Second class Upper")
 elif cgpa >= 2.5:
  print(f"{name} is on Second class Lower")
 elif cgpa >= 1.5:
  print(f"{name} is on Third class")
 elif cgpa < 1.5:
  print(f"{name} is on fail")
 else:
  print("No record found....")

# Welcome message 
print("Welcome to my CGPA Calculator.....")

# Looping the program for more accessibility 
while True:
 print("Input Check GPA to check cgpa and use exit to close program")
 user = input("GPA or Exit: ").lower()
 if user == "exit":
  print("Good luck")
  break
 elif user == "gpa":
  name = input("Input student name: ").lower().capitalize()
  try:
   matric_number = int(input("Input Student Matric number: "))
  except:
   print("Error. Please input only numbers")
   matric_number = int(input("Input Student Matric number: "))
  size = int(input("Enter number of course: "))
  countdown = 1
  countdown2 = 1
  courses = []
  score = []
  for i in range(size):
   courses.append(input(f"Enter course code{countdown}: ").lower().capitalize())
   countdown += 1
  for i in range(size):
   score.append(int(input(f"Enter Score for {courses[i]}: ")))
   countdown2 += 1
   
  print()
  print()
   
  for i in range(size):
   print(f"{score[i]} in {courses[i]}")
   time.sleep(0.7)
 
  print()
  print()
  
  word1 = "Processing......."
  word2 = "Calculating......."
  word3 = "Finishing........."
   
  total_gp = 0
  for s in score:
   total_gp += gpa_determine(s)
  cgpa = total_gp / size
  
  for w in word1:
   print(w,end="",flush=True)
   time.sleep(0.09)
  
  for o in word2:
   print(o,end="",flush=True)
   time.sleep(0.09)
   
  for r in word3:
   print(r,end="",flush=True)
   time.sleep(0.09)
   
  print()
  print()
  print("CGPA is ready")
  time.sleep(1)
  
  print(f"{name} has the CGPA of: {cgpa:.2f}")
  class_grade(cgpa)
  
  print()
  print()
  print()
  
 else:
  print("Invalid Input Please choose correctly")
  
