"""
A school wants a simple Python program that can help a teacher calculate a student's academic performance. The program should ask the teacher to enter the student's name, Mathematics marks, Programming marks, and Networking marks. After receiving the information, the program should calculate the student's total marks and average mark and display a clear summary showing the student's name, total marks, and average.
"""

# INPUT - record the input from the user
student_name = input('Student name: ')
math_marks = input("Enter maths marks: ")
programming_marks = input("Enter programming marks: ")
network_marks = input("Enter networking marks: ")

# calculate the students total marks
# typecasting 
# string to int
# int()
total_marks = int(math_marks) + int(programming_marks) + int(network_marks)
average  = total_marks // 3


# display the students details
print(f"STUDENT DETAILS\t\n Student's name {student_name}\t\n Total marks {total_marks}\t\n Average marks {average}\n")






# swapping 
user_age = 45
user2_age = 60

# swap the ages of the two users
# pointers
user_age, user2_age = user2_age, user_age 

username, gender, age, career = "John", "Male", 18, "IT"

# print(f"{user2_age}\t\n {user_age}")

