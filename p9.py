# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

i=1
a=[]
b=[]
while i<=30:
    c=i**2
    if i <=5:
        a.append(c)
    elif i>25:
        b.append(c)
    i=i+1
print(a)
print(b)