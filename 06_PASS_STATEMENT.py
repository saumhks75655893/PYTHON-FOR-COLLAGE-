# 7.3 - Write a python program to demonstrate pass statement. 
# pass is used when programmer don't want to do anything at that moment. 

n = int(input("Enter the number : "))

for i in range(1,n+1): 
    if(i==4): 
        pass
    else:
        print("Odd numbers is : ", i)
        
def man():
    pass
