# Question 6

# Yeh question 3 parts mein. Teenon parts ka code likh ke ek hi file mein submit karo.
# Question (Part 1)
# calculator naam ka ek function banao jo teen argument leta ho - number_x, number_y, operation. 
# number_x aur number_y mein hum humesha do integers denge aur operation mein kaunsa operation karna 
# hai woh denge. Jaise:
# Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna karega.
# Agar operation mein "subtract" diya toh number_x aur number_y ko subtract kar ke return karenge.
# Agar operation mein "multiply" diya toh number_x ko number_y se multiply kar ke returna karega.
# Agar operation mein "divide" diya toh number_x ko number_y se divide kar ke return karega
# Neeche kuch function calls ke examples diye hue hain:
#     calculator(20, 25, "add") call karne pe 45 returna karega. 45 hume 20+25 karne se milega.
#     calculator(40, 3, "subtract") call karne pe 37 return karega. 37 hume 40-3 karne se milega.
#     calculator(10, 4, "multiply") call karne pe 40 return karega. 40 hume 10*4 karne se milega.
#     calculator(40, 4, "divide") call karnse pe 10 return karega. 10 hume 40/3 karne se milega.
# Function likhne ke baad, yeh kaam karne ke liye function call karo aur variable mein value daalo.
#     24 aur 20 ko add karo aur number_1 variable mein value daalo
#     50 aur 60 ko multiply karo aur number_2 variable mein value daalo
#     80 aur 120 ko divide karo aur number_3 variable mein value daalo
#     90 aur 23 ko subtract karo aur number_4 variable mein value daalo
# Question (Part 2)
# # Ab input ka use kar ke user se 2 numbers input lo.
# # Note: Yeh karne ke liye koi function banane ki zaroorat nahi hai.
# Fir calculator function ko 4 baar call call kar ke inn dono numbers do add, 
# subtract, multiply, divide karo aur result ko 4 alag variables mein daalo. Woh 
# variables ka naam yeh hoga:
# add_result add operation ka result store karega
# subtract_result subtract operation ka result store karega
# multiply_result multiple operation ka result store karega
# divide_result divide operation ka result store karega
# Fir upar wale chaaron variables ko print karo.
# Final code ko submit karo :)
# Question (Part 2)

# list_change naam ka ek function ka code likho jo 2 lists jisme 
# integers arguments ki tarah le aur fir unn lists ki woh items jo 
# same index number (kram) pe hain unko multiply kar ke ek nayi list return karvaye.

# Aapko multiply karne ke liye calculator function ka use karna hai. 
# Normal tareeke se multiply nahi kar sakte ho.

# Jaise agar hum function ko aise call karenge toh:

def calculator(number_x,number_y,oprator):
   number_1=int(input("enter the number:"))
   number_2=int(input("enter the number:"))  
   if oprator=="add":
    number_1=number_x+number_y
    return number_1
   if oprator=="subtract":
      number_2=number_x-number_y
      return number_2
   if oprator=="multiply":
      number_3=number_x*number_y  
      return number_3
   if oprator=="divide":
      number_4=number_x/number_y 
      return number_4
print(calculator(20,25,"add"))
print(calculator(24,20,"add_result"))  
print(calculator(40,3,"subtract"))    
print(calculator(50,60,"subtract_result")) 
print(calculator(10,4,"multiply"))    
print(calculator(80,120,"multiply_result"))    
print(calculator(40,4,"divide"))    
print(calculator(90,23,"divide_result"))    
       

def calculator(number_x,number_y,oprator):
   number_1=int(input("enter the number:"))
   number_2=int(input("enter the number:"))  
   if oprator=="add":
    number_1=number_x+number_y
    return number_1
   if oprator=="subtract":
      number_2=number_x-number_y
      return number_2
   if oprator=="multiply":
      number_3=number_x*number_y  
      return number_3
   if oprator=="divide":
      number_4=number_x/number_y 
      return number_4
