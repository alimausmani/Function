# Question 5

# Ek function likhiye jo ki ek limit naam ka parameter 
# lega aur 0 se limit tak ke beech ke number jo ki 3 aur 
# 5 ke multiples hain unka sum print karega.jaisa ki niche dikhaya gya hai.

# Input:-
# 10
# 3 aur 5 ke multiples => 3, 5, 6, 9, 10

# Output :-
# 33


def limit(n=10):
    i=1
    sum=0
    while i<=n:
        if i%3==0 or i%5==0:
            sum=sum+i
            print(i,end=", ")
        i=i+1
    print() 
    print(sum)
limit()        

