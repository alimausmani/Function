# Q28. Write a function called showNumbers that takes a parameter called limit. It should print
# all the numbers between 0 and limit with a label to identify the even and odd numbers. For
# example, if the limit is 3, it should print: - 0 even,1 odd, 2 even, 3 odd .

def shownumbers(l):
    i=0
    even=0
    odd=0
    while i<=(l):
        if i%2==0:
            even+=1
            print("even",i) 

        else:
            odd+=1
            print("odd",i)         

        i+=1       
shownumbers(3)              