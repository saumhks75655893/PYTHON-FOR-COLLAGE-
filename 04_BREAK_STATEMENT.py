# 7.1 - Write a python program to demonstrate the break statement. 

n = int(input("Enter the number : "))

for i in range(1,n+1): 
    if(i == 10): 
        break
    else:
        print(f"{i} is : ", i)
    