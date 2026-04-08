print("Hello World")


#Type Casting 

## To convert variables from one data type to another 
## int() , float() , str() , bool() , list() , tuple() , dict() , set()

### Exercise 1 

length = int(input("Enter length of rectangle "))
width = int(input("enter width of rectangle "))
area  = length* width 
print(f"area of the reactangle is {area} ")


### Exercise 2 
item = str(input("what would you like to purchase? "))
price = float(input("enter the price:"))
quantity = int(input("How many would you like to purchase"))
bill = price * quantity 
print(f"this costs ${bill} dollars ")
print(f"you have purchased {quantity} {item}/s")


### arithmatic operators 
### add is +=
### sub is -=
### divi is /=
### multipli is *= 
### power is ** 
### absoulute value is abs(num) 
### max and min are max(x,y,z), min(x,y,z)
### remainder is num1%num2
### int divi is num1//num2


y=5
y*=3
y/=3
y+=3
y-=3 ### ( final value will be 5)


import math 

print(math.pi)
print(math.e)
print(math.sqrt(9) )



### Exercise 3 calculate circumfrence of a circle 
import math 
x= math.pi
y = float(input("enter the radius of the circle :"))
area = x*(y**2)
print(f"the area of the circle is {round(area,4)}")
circ = x*y*2
print(f"the circumfrence of the circle is {round(circ,3)}cm**2")



### Exercise 4 
import math 
a = float(input("Enter the length of the shortest side "))
b = float(input("Enter the length of the seconds largest side "))
c = math.sqrt(pow(a,2)+pow(b,2))
print(f"the length of the hypotenuse is {round(c,3)}cm")



### coditional statements (if,elif,else)

age = int(input("enter your age"))
if age>=18:
    print("you are eligible to vote now")
elif age<0:
    print("you dont exist ")
else:
    print("you are too young dumbass")



name = str(input("please enter your name"))
if name =="bro":
    print("you are sigma ")          ### it is not necesary to have and if and
                                     ###  else condition together only if works perfectly fine 





### Logical Operators ( and , or not )
### and = both conditions must be true
### or = atleast one condition must be true 
### not = the oposite of the input is true 

### Basic program using logcal operators

temp = float(input("enter the value of the  temperature "))
if temp>20 and temp<30:
    print("it is warm outside ")
elif temp<0:
    print("its cold asf outside ")
elif temp<20 or temp>10:
    print("it is chilly  outside ")
elif not temp<30:
    print("its hot outside")



### condition expressions(ternary operator)
### writitng one line of code to define an if else conditional statement and give a true output
### X if condition else Y 

num = 5 
print("it is positive" if num>0 else "it is negative" )




### traditional method 
num = int(input("enter a number "))
if num>0:
    print("this is a positive integer")
else :
    print("this is a negative integer")

### Shortcut method , print or assign the expression 
### expression should be in the form of (X if condition else Y)
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))


### ALL examples of this conecept
print("positive" if num>0 else "negative")
print("even" if num%2==0 else "odd")
max_num = "max" if num1>num2 else False
print(max_num)
min_num = "min" if num1<num2 else False
print(min_num)
print("positive" if num>0 else "negative")
print("even" if num%2==0 else "odd")
max_num = "max" if num1>num2 else num2
print(max_num)
min_num = "min" if num1<num2 else num2
print(min_num)


###  usefull string functions 
variable = "bro code"

variable.find("b")
variable.rfind("o")
variable.count("o")
variable.capitalize()
variable.index("d")
print(variable.find("b"),variable.rfind("o"),variable.count("o"),variable.capitalize(),variable.index("d"))
variable.isalpha()
variable.isdigit()
variable.replace(" ",".")





### validate user input
user_name = str(input("enter a word"))
if len(user_name)<11 and user_name!= " " and " "  not in user_name and not  type(user_name)==str:
    print("this is a valid username")
else:
    print("this is an invalid username")
### suposed to write with string fucntions but i didnt understand 
### how to so did with logical operators instead



### String indexing 
### accesing specific elements of a string using [start:end:step] format

num="1233456797,1204566"
num[0]
num[0:4]
num[4:12]
num[0:12:2]
num[5:]
num[-1]
print(num[0],num[0:4],num[4:12], num[0:12:2],num[5:],num[-1])

creitcard_num = str(input("enter your credit card number ,"))      
print(creitcard_num[-4:])
### Remmeber to define your input as a string cuz python only allows indexing for strings 



### Format specifiers in python
import math
num = math.pi
print(f"this is {num:.2f}")
print(f"this is {num:^}")
print(f"this is ${num:.2f}")
print(f"this is {num:.2f}")
print(f"this is {num:< .2f}")




### while loops 
### coumpound interest calculator 
r=1;n=1;p=1
while r>0 and n>0 and p>0:
    r = float(input("enter your interest rate in % :"))
    n = int(input("enter the number of years you would like your amount to be compounded"))
    p = float(input("Enter the amount you are starting with"))
    new_amount = p*(1+(r/100))**n
    print(round(new_amount,2))

### print(round(new_amount,2))
    


if r<=0 or p<=0 or n<=0:
    print("you have entered  an invalid input")


### for loops
### can iterate over an array ,string , sequence
for i in range(0,10):
    if i ==5:
        continue
    print(i)
    




### nested loops 

rows = int(input("enter the number of rows you would like in your rectangle:"))
columns = int(input("enter the number of columns you would like in your rectangle"))
for x in range(rows):
    for i in range(columns):
        print(i, end = "")
    print()



### collections = single variable stores multiples values
### List = [] ordered and changeable , duplicated are ok
### Set = {} unordered and immutable but add/remove ok , NO DUPLICATES
### tuple = () ordered and unchangeable , Duplicates ok , FASTER

###ALL INBUILT FUCNTIONS OF LISTS 
### lst.append and lst.insert are used to add items , apeend will add at the end of the list but 
### in insert you may specify the specific index location where you would like to insert your item 
### lst.remove will delete the first occurance of the item in a list 
### lst.pop is used to remove and return the last item in a list .
### lst.index (element) will show the corresponding index of said element in the list 
### lst.count(element) will show you how many times that element apeears in the list
### lst.sort will sort the list in alphebatical order or asc order
### lst.reverse will reverse the order of the list 
### lst.clear deletes all elements of the lst 






### Sets
fruits = {"apple","banana","orange","pineapple"} ### are unordered so  no indexing

fruits.add("watermelon")
fruits.remove("apple") ### can only add or remove elements
print(fruits) ### sets are immutable you can add or remove elements but you cant edit the elemnts themselves
print("pineapple" in fruits)      ### use in to see if something exists in a collection


### tuple are ordered and unchangable like ARRAYS in C
fruits = ("apple","banana","orange","pineapple")
print(fruits)
print(fruits.index("pineapple"))
print(fruits.count("apple"))
fruits.remove("apple") ### As you can see an error will come a tuple cant be altered like a list or set






















































