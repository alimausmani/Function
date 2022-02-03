# Question 1

# eligible_for_vote name ka function likho jo ki user ko bataye 
# ki vo (he/she) vote de sakta hai ya nahi. ( Consider minimum age of voting to be 18. )

def eligible_for_vote():
    user=int(input("enter your age:"))
    if user>=18:
        print("you are eligible for vote")
    else:
        print("you are not eligible for vote") 
eligible_for_vote()           