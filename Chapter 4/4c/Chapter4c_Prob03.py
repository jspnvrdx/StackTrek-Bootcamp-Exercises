import os
os.system('cls||clear')

#----CODE STARTS HERE------

grade = float(input())

if grade >= 0.0 and grade <= 10.0:
    if (grade % 1 != 0.5) and (grade % 1 != 0.0):
        print ("Grades should be rounded to the nearest half point.")
    elif grade <= 10 and grade >= 8.5:
        print("Grade A")
    elif grade <= 8 and grade >= 7.5:
        print("Grade B")
    elif grade <= 7 and grade >= 6.5:
        print("Grade C")
    elif grade <= 6 and grade >= 5.5:
        print("Grade D")
    elif grade < 5.5 and grade >= 0:
        print("Grade F")
else:
    print("Grades should be between zero and 10.")