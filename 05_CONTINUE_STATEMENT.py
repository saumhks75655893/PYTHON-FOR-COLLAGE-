# 7.2 - Write a program to demonstrate the continue statement. 

n = int(input("Enter the number : "))

for i in range(1,n+1): 
    if(i%2==0): 
        continue
    else:
        print("Odd numbers is : ", i)