# Q1.Write a Python program to count the number of strings
# where the string length is 2 or more and
# the first and last characters are the same from
# a given list of strings.
# ist=['abc', 'xyz', 'aba', '1221']
# result=2


def count_number():
  a= ['abc', 'xyz', 'aba', '1221','abccba']
  count=0
  for i in a:
   if (len(i)>=2 and i[0]==i[-1]):
    count=count+1
  print(count)
count_number()    