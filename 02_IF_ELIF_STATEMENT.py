# 6.2. Write a python program to print your grade . 
''' formate of the grade is : 
 if marks is greater than 90 print grade a
 if marks is greater than 75 and less than 90 than print grade b
 if marks is greater than 60 and less than 75 than print grade c . '''

marks = int(input("Enter the marks : "))

if marks >= 90 : 
    print("Grade A")
elif marks >=75 and marks <90: 
    print("Grade B")
elif marks >= 60 and marks < 75: 
    print("Grade C")