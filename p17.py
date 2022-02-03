# Q17. Write a function to tell user if he/she is able 
# to vote or not.( Consider minimum age of voting
# to be 18. )

def able_for_vote():
    num=int(input("enter the number:"))
    if num>=18:
        print("he/she is able to vote")
    else:
        print("he/she is not able to vote") 
able_for_vote()           