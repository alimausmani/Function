# Q49. Write a flowchart which takes an input N. Then input N numbers. Then for each of the N numbers, print
# “even” if the number is even or and “odd” if the number is odd.
# Sample input:
# 7
# 1
# 4
# 23
# 95
# 1203
# 403
# 84
# Sample output:
# Odd
# Even
# Odd
# Odd
# Odd

# Odd
# Even

def even_odd(n):
    n=int(input("enter the number:"))
    even_count=0
    odd_count=0
    i=1
    while i<=n:
        if i%2==0:
            print("even number=",i) 
        else:
            print("odd number=",i)
        i+=1    
even_odd(5)              