# 8.1 - Take 10 integers from keyboard using loop and print their average value on the screen.

num = 0
for i in range(1,11): 
    number = int(input("Enter the number : "))
    num = num + number 
    
avg = num / 10

print("Total of all 10 numbers : ",num)
print("Average value of given 10 numbers is : ",avg)