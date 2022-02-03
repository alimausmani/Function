# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

def removezero(num):
    num=list(str(num))
    length=len(num)
    i=length-1
    final=""
    while i>=0:
        if num[i]=='0':
            num[i]=""
        else:
            break
        i=i-1
    return"".join(num)
print(removezero(1450))
print(removezero(960000))
print(removezero(1050))
print(removezero(1050))