
//This program reads in a student's last name and final grade.

#Ask for student's last name
last_name = input("please enter your name: ")
#Ask for student's final grade
final_grade = int(input("please enter your final grade: "))
#Determine pass or fail
if final_grade >= 50:
    print(f"hello {last_name}, you passed this class")
else:
    print(f"Hello {last_name}, you failed this class")




