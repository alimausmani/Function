# Question 2

# Ek perfect() naam ka function define kijiye jo ki ek 
# parameter lega aur uss parameter ko hume check karana hai 
# ki vo perfect number hain ya nahi. Iske baad uss function ko use 
# karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers ko
# print kare.[ hum ek aise integer number ko perfect number kahenge jo ki uske
# sabhi factors ( including 1 & excluding itself) ka sum uss number ke barabar hota hai.

def perfect(n):
    i=1
    while i<1000:
        j=1
        sum=0
        while i>j:
            if i%j==0:
               sum+=j
            j+=1
        if i==sum:
            print(i,"-","it is a perfect number") 
        i+=1    
perfect(1000)                  
