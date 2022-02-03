# Question 7

# Ek function define karo jo ki input me 2 strings lega aur
# dono strings me se jiski length jyaada hogi use print karega
# aur agar dono strings ki length equal hui to dono ko line by line 
# print karega . Hint :- use len() builtin function..

# Input:-

# function_name(“hello”,”welcome”)
# function_name(“sonu”,”monu”)

# Output :-

# welcome
# sonu
# monu

def name_string():
    A = input("enter a name:")
    J = input("enter a name:")
    if len(A)>len(J):
        print("hello welcome",A)
    elif len(A)<len(J):
        print("hello welcome",J)
    else:
        print("hello welcome",A,J)
name_string()        

