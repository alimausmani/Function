# Question (Part 1)

# check_numbers naam ka ek function likhiye jo do numbers le aur fir 
# print kare "Dono even hain" agar dono numbers even (2 se divide hote hain) 
# nahi toh print kare "Dono numbers even nahi hai"

# def check_numbers():
#     num=int(input("enter the number:"))
#     n=int(input("enter the number:"))
#     if num%2==0:
#         print("even")
#         if n%2==0:
#             print("dono even hai")
#     else:
#         print("Dono odd hai")
# check_numbers()         

# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko 
# arguments ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi.

# Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo.

# Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] 
# Toh usko yeh output deni chaiye:

# dono even hain
# ---------------
# dono even nahi hai
# ---------------
# dono even hain
# ---------------
# dono even hain
# ---------------
# dono even nahi hain
# ---------------
# dono even nahi hain

    
def add_numbers_list(s,n):
    i=0
    while i<len(s):
        if s[i]%2==0 and n[i]%2==0:
            print("both are even")
        else:
            print("both are not even")  
        i+=1      
add_numbers_list([2,6,18,10,3,75],[6,19,24,12,3,87])    


