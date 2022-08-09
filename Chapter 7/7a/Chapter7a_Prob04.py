import os
import pickle
os.system('cls||clear')

#----CODE STARTS HERE------
def student75():
    student = open('student.dat', 'rb')

    if os.path.exists('students above 75.dat'):
        new_student = open('students above 75.dat', 'wb')
    else:
        new_student = open('students above 75.dat', 'xb')
        new_student = open('students above 75.dat', 'wb')

    student_data = []
    while True:
        try:
            participant = pickle.load(student)
            if participant[2] > 75:
                student_data.append(participant)
        except:
            break
    
    for i in student_data:
        pickle.dump(i,new_student)
# ----------- Uncomment below if you want to check the display in basket.dat -----------

    # new_student = open("students above 75.dat", "rb")
    # while True:
    #         try:
    #             participant = pickle.load(new_student)
    #             print(participant)
    #         except EOFError:
    #             break
    
    student.close()
    new_student.close()

student75()