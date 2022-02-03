# Q13.Write a function to check if a number is even or not.

def even_number(num):
    i=0
    while i<3:
        num=int(input("enter the number:"))
        if i%2==0:
            print("even number") 
        else:
            print("odd number")     
        i+=1
       
even_number(3)            
