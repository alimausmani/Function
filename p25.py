# Q25. Given a list of numbers, write a Python program to count
# positive and negative numbers in a List using
# function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

def positive_negative_count():
    list1=[2,-7,5,-64,-14]
    pos_count=0
    neg_count =0
    num=0
    while (num<len(list1)):
        if list1[num]>=0:
            pos_count+=1
        else:
            neg_count+=1
        num+=1
    print("positive number in the list: =",pos_count) 
    print("positive number in the list: =",neg_count)    
positive_negative_count()       
              
