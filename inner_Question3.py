# Question 3

# Ek function banaiye jo 3 numbers ka sum aur average print kare.
# Hum user se 3 number input karwayenge aur fir unn 3 numbers ka sum 
# aur average print karwayenge jaisa ki niche output diya hua hain.

# Input:-

# enter first number :-3
# Enter second number :-4  
# Enter third number:-5    
# Output :-
# Sum of three numbers :-12
# Average of three numbers :-4

def sum_avrg():
   i=0
   sum=0
   avrg=0
   while i<3:
       b=int(input("enter any number:"))
       sum=sum+b
       avrg=sum//3
       i+=1
   print(" sum =",sum,"\n","average=",avrg)   
sum_avrg()   



