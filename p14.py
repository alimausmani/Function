# Q14.Write a function to check if a number is prime or not.

def check_prime_number():
    num=int(input("enter any number:"))
    i=2
    f=0
    while i<num:
        if num%i==0:
            print(i)
            f+=1
        i+=1
    if f==0:
        print("it is a prime anumber")
    else:
        print("it is not a prime number") 
check_prime_number()                   