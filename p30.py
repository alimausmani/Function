# Q30. Write a function that prints all the prime numbers between 0 and limit where limit is a
# parameter.


def prime_numbers(num):
    num=int(input("enter the number:"))
    i=2
    f=0
    while i<num:
        if num%i==0:
            f+=1
        i+=1
    if f==0:
        print("it is a prime number",i)
    else:
        print("it is not a prime number")
prime_numbers(20)      


# def prime_numbers(i):
#     i = 2 
#     while i < 20:
#      j = 1
#      c = 0
#     while j < i:
#         if i%j == 0:
#             c+=1
#         j+=1
#     if c==1:
#         print("prime",i)
#     i+=1
# prime_numbers(2)    

