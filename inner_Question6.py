# Question 6

# Ek function define kijiye jo ki drivers ki speed check karega. 
# Aur ye function speed naam ka ek parameter lega.
# Agar speed 70 se kam hai to ye “ok” print karega.
# Agar driver ki speed 70 se jyaada hai to function use har 5 km ke
# liye 1 point dega (ye 70 ko count nahi karega).
# example ke liye agar speed 80 hai to print karega “points:2” .
# Agar driver ko 12 points se jyaada points milte hai to , 
# function “License suspended” print karega.

# Input:-

# 85
# 135

# Output :-
# 3
# “License suspended”

def speed_check():
    i=0
    n=int(input("enter the number:"))
    if n<=70:
       print("ok")
    elif n>=70:
         print("one points:2")
         points=int(input("enter the points:"))
         if n>=12:
           print("License Suspended")
    else:
        print("not")
        
speed_check()


# def speed():

#   limit=int(input("enter the number:"))
#   i=0
#   while i<1:
#     j=70
#     points=0
#     while j<limit: 
#      if limit>70:
#         points+=1
#      j+=5
#     if points<=12 and limit>70:
#       print("points:",points)
#     if limit<=70:
#       print("ok")   
#     elif points>12:
#         print("license suspended")
#     i=i+1
# speed()
