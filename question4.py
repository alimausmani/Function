

# add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le 
# aur fir unka sum print karta hai. Arguments ka naam number1 aur number2 hona chaiye.

# Input :-

# num1 = 56

# num2 = 12

# add_numbers(num1,num2)

# Output :- 68

# def add_numbers(num1=56,num2=12):
#     print(num1+num2)
# add_numbers()

# Question (Part 2)

# add_numbers_list naam ka function likhiye jo do integers ki 2 
# lists leta ho aur fir same position wale integers ka sum print karta ho.

# Same position waale 2 integers ka sum karne ke liye Part 1 mein 
# di gayi add_numbers waale function ka use karo.

# Jaise agar hum iss function ko [50, 60, 10] aur
# [10, 20, 13] denge ko woh yeh print karega

# 60
# ---------------
# 80
# ---------------
# 23
# ---------------

def add_numbers_list(list1,list2):
    i=0
    while i<len(list1):
        print(list1[i]+list2[i]) 
        i+=1   
add_numbers_list([50,60,10],[10,20,13])    


    