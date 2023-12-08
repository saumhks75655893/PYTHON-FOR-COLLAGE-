# 6.3. Write a python program to print that the person is senior citizen or Young man or Teenage or Child on the basis of age. 
''' formate of the age is : 

if age is greater than or equal to 60 than The person is senior citizen. 
if age >= 25 and < 55 than The person is young man. 
if age >= 15 and < 25 than the person is teenager. 
else the person is a child.
  '''

age = int(input("Enter the age : "))

if age>=60: 
    print("The person is a Senior citizen of India. ")
elif age>=25 and age<60: 
    print("The person is a Young man.")
elif age>=15 and age<25: 
    print("The person is a Teenager Boy.")
else:
    print("The person is a Child.")