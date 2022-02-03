# Q2.Write a Python function to find the Max of three numbers.

def max_number():

 num1=int(input("enter the number:"))
 num2=int(input("enter the number:"))
 num3=int(input("enter the number:")) 
 if num1>num2 and num1>num3:
     print("it is a greater number:",num1)
 elif num2>num1 and num2>num3:
     print("greater number:",num2) 
 else:
     print("greater:",num3)       
max_number()    

