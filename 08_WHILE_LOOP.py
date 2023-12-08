# 8.2 Write a C++ program to calculate factorial of a given number.

num = int(input("Enter the number : "))

fact = 1
while(num!=0): 

    fact = fact * num
    num = num - 1
    
    
print(f"Factorial of {num} is : {fact}")

# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1 > num2: 
    a = num1
else:
    a = num2
i=2
while(i<=a): 
    if(num1 % num2 == 0): 
        print("GCD is : ",num2)
        break
    elif num2%num1==0: 
        print("GCD is : ",num1)
        break
    elif(num1%i==0 and num2%i==0):
        print("GCD is : ", i)
        break
    else: 
        print("GCD is : ", 1)
        break
    i = i+1
        