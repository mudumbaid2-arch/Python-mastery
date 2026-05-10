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



### dictionaries 

menu = {"pizza" : 3.00,  
        "nachos": 2.50,
        "pasta" : 5.99,
        "chips" : 3.0,
        "samosa": 5.50}
total = 0
cart = []
for item , price in menu.items():
    print(f"{item}:{price}")

while True:
    food = str(input("enter your food of choice "))
    if menu.get(food) is not None:
        cart.append(food)
    elif food=="q":
        break


print(cart)

for food in cart:
    total = total+menu.get(food)
    print(food , end = " ")
print()

print(f"total is {total:.2f}")




### Number guessing game

import random 
low = int(input("enter the lower limit "))
high = int(input("enter the higher limit "))
count =0
answer = random.randint(low,high)
flag = True
while flag:
    guess = int(input(f"enter your guess between {low} and {high} "))
    count+=1
    if guess > answer:
        print("your guess was too high please try again ")
    elif guess<answer:
        print("your guess was too low please try again ")
    elif guess>high or guess<low:
        print("the number you have chosen is out of range please try again ")
    elif guess==answer:
        flag = False
      

        
print(f"you finally guessed the correct number {guess} , congrats!!!")
print(f"you took {count} guesses to get it right")




### functions
### are blocks of reusable code 
### default values in a function can be replaced when passing an argument
### makes your function more flexible and less typing
### default argument always follow non default arguments
### 
def bill(price ,discount=0,tax=0.10):
    return price*(1-discount)*(1+tax)

print(bill(40))
print (bill(40,0.25,0.2)) 
### you may redefine the arguments as you wish whenever your calling your function

import time
def count(high , low=0): ##3 always assign a default argument AFTER A NON DEFUALT ONE
    for x in range(low,high+1):
        print(x)
        time.sleep(0.5)
    print("DONE!")
print(count(1,10))
print(count(30))
print(count(30,19))



### KEYWORD ARGUMENTS
def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phonenum= print(get_phone(91,420,853,4669))
print(get_phone(country=800,last=900,first=50,area=400))
### as long as u define the argument your assigning you may assign the value in any order you wish



### Iterables 
### lists tuples sets and dictionaries and strings
my_dictionary = {"a":1,"b":2,"c":3}
for key in my_dictionary:
    print(key , end=" ")          ### output a b c
for value in my_dictionary.values:
    print(value , end = " ")      ### output = 1 2 3
for key,value in my_dictionary.items():
    print(f"{key}={value}")




### Membership operators 
### in and not in
### Tests to see if a value is present in a string/collection
secret_word = "apple"
guess = str(input("guess a letter that you think is present in the secret word"))
if guess in secret_word:
    print(f"the letter {guess} is present in the secret word")
else:
    print(f"the letter {guess} is  not present in the secret word")





### list comprehensions
lst =[]
for i in range(1,11):
    lst.append(i)
print(lst)

### using list comprehension 
lst1 =[i for i in range(10)]        ### can create a list/set using just one line of code
print(lst1)

lst2 = {j for j in range(20) if j%2==0}     ### can even put conditional statements when creating the list/set
print(lst2)

squares = [x**2 for x in range(10)]
print(squares)

even_squares =[y**2 for y in range(10) if y%2==0 ]
print(even_squares)

### match case statements
### it is used to replace many if and elif statements with a much more legible syntax

def calories_burned(activity,speed,weight,duration):
    if activity == "running" and speed <=8:
        caloriesburnt= 8.3*weight*duration
        return caloriesburnt
    elif activity == "running" and 8<=speed<=10:
        caloriesburnt = 9.8*weight*duration
        return caloriesburnt
    elif activity == "running" and 10<=speed<=12:
        caloriesburnt = 11.5*weight*duration
        return caloriesburnt
    elif activity == "running" and 12<=speed<=14:
        caloriesburnt= 12.8*weight*duration
        return caloriesburnt
    elif activity == "cycling" and 14<=speed<=16:
        caloriesburnt = 4*weight*duration
        return caloriesburnt
    elif activity == "cycling" and 16<=speed<=20:
        caloriesburnt=8*weight*duration
        return caloriesburnt
    elif activity == "cycling" and 22<=speed<=25:
        caloriesburnt = 10*weight*duration
        return caloriesburnt
    elif activity == "walking" and speed <=3:
        caloriesburnt = 2.5*weight*duration
        return caloriesburnt
    elif activity == "walking" and  3<= speed <= 4 :
        caloriesburnt = 3.5*weight*duration
        return caloriesburnt
    elif activity == "walking" and 4<= speed <= 5.5:
        caloriesburnt = 5*weight*duration
        return caloriesburnt
    else:
        return "Error: The activity/speed you have chosen is not supported."





### An alternative to using many elif statements
### as you can see in the new and improved version it uses each activity 
### as the specific case and then segregates accordingly making it wayy cleaner
### syntax = match case return case
### case_ is a wild card statement it will execute if the previous cases
###  arent satisfied like an else block
def calories_burned(activity,speed,weight,duration):
    match activity:
        case "running":
            if speed <= 8:
                caloriesburnt = 8.3 * weight * duration
            elif 8 <= speed <= 10:
                caloriesburnt = 9.8 * weight * duration
            elif 10 <= speed <= 12:
                caloriesburnt = 11.5 * weight * duration
            elif 12 <= speed <= 14:
                caloriesburnt = 12.8 * weight * duration
            else:
                return "Error: The activity/speed you have chosen is not supported."
            return caloriesburnt
        case "cycling":
            if 14 <= speed <= 16:
                caloriesburnt = 4 * weight * duration
            elif 16 <= speed <= 20:
                caloriesburnt = 8 * weight * duration
            elif 22 <= speed <= 25:
                caloriesburnt = 10 * weight * duration
            else:
                return "Error: The activity/speed you have chosen is not supported."
            return caloriesburnt
        case "walking":
            if speed <= 3:
                caloriesburnt = 2.5 * weight * duration
            elif 3 <= speed <= 4:
                caloriesburnt = 3.5 * weight * duration
            elif 4 <= speed <= 5.5:
                caloriesburnt = 5 * weight * duration
            else:
                return "Error: The activity/speed you have chosen is not supported."
            return caloriesburnt
        case _:
            return "Error: The activity/speed you have chosen is not supported."




### modules 
### is a file containing specific data/code that you want to implement in your program
### you call a module using the 'import' key word
 

import math as m
### print(math.pi) ### you can give the module you wanna import a nickname 
### if your too lazy to type the entire thing but you must use that nickname to call 
### values or functions from that module or else an eror will come
print(m.pi)     ### this will run properly as you have nicknamed the module 


### variable scope where a variable is visible and accessable
### scope resolution local -> global -> enclosed -> built in (LEGB)
### in prgrams the variables you define will output the value based on the LEGB order 



### encryption program 
import random
import string
chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
### print(chars)
key = chars.copy()
random.shuffle(key)
### print(key)
decrypted_word= []
encrypted_word = []
### for encryption 
word =list(input("enter a word "))
for char in word:
    position=chars.index(char)
    char=key[position]
    encrypted_word.append(char)
print(f"original word is {word}\n")
print(f"encrypted word is {encrypted_word}\n" ) 


### for decryption
for char in encrypted_word:
    position=key.index(char)
    char=chars[position]
    decrypted_word.append(char)
print(f"decrypted word is {decrypted_word}\n")


### rock paper scissors game
import random
options = ("rock","paper","scissors")

flag = True
while flag:
    
    player1 = str(input("enter an option(rock, paper, or scissors and q to quit) ")).lower()
    player2 = random.choice(options)
   
    if player1=="q":
        print("thanks for playing hope you had fun")
        flag=False
    elif player1=="rock" and player2=="paper" or player1=="paper" and player2=="scissors" or player1=="scissors" and player2=="rock":
        print("player 2 has won")
        print(f"computer chose: {player2}")
    elif player2=="rock" and player1=="paper" or player2=="paper" and player1=="scissors" or player2=="scissors" and player1=="rock":
        print("player 1 has won")
        print(f"computer chose: {player2}")
    elif player1 not in ( "rock" , "paper", "scissors" , "q") and player2 not in ( "rock", "paper",  "scissors" , "q" ):
        print("please choose an apropriate option and try again")
    elif player1 == player2 :
        print("this is a draw please try again")


### arbitrary arguments means the function will allow a varying number of arguments
### *args = multiple arguments and **kwargs = multiple key word arguments
def add(*args):  ### replace parameters with *args to accept N number of parameters
    total = 0
    print(type(args))
    for num in args:
        total=total+num
    print(total)
add(1,2)


def display_name(*names):
    for name in names:
        print(name)
    print()


### ---- SHIPPING LANE PROGRAM ----
### *args   = ship multiple packages (varying number of items)
### **kwargs = shipping details (destination, priority, weight etc.)

def ship_order(order_id, *packages, **details):
    print(f"\n ORDER ID: {order_id}")
    print("   Packages being shipped:")
    for package in packages:
        print(f"     - {package}")
    print("   Shipping Details:")
    for key, value in details.items():
        print(f"     {key}: {value}")
    print("-" * 35)

# single item, basic details
ship_order(1001, "laptop", destination="Mumbai", priority="standard")

# multiple items, more details
ship_order(1002, "shoes", "shirt", "watch", destination="Delhi", priority="express", weight="2.3kg", fragile=False)

# one heavy package with extra notes
ship_order(1003, "refrigerator", destination="Chennai", priority="standard", weight="45kg", fragile=True, notes="handle with care")




### oop
### an object is a group of related  atributes (variables) and methods (functions)
### Ex : phone, book, cup ,glass, calculator 
### method = function that belongs in an object / what the object can actually do 
### for the phone it can be turn on/off make a call etc etc
### methods simply define what and object can do and u write the logic 
### for that program as a function
### an atribute is something about the object /description of the object 
### You need a "class" to create and store many objects
### class = is the blueprint used to design the structure and layout of the object
### MAIN goal define what our object has (atributes) and what it can do (methods)


class car:
    def __init__(self,name,engine_type,color ,year):
        self.name = name
        self.engine_type = engine_type
        self.color = color
        self.year = year
    ### Methods : they define what an object can do 
    def speed(self,velocity):
       
        if velocity>60:
            print(f"you are driving the {self.year} {self.color} {self.name}  too fast , please slow down immediately")
        else:
            print(f"you are driving the {self.year} {self.color} {self.name} responsibly carry on")

    def is_driving(self):
        return True
    def is_notdriving(self):
        return True
    def is_drinking(self):
        print(f"you must never drive like that especially with a  {self.year} {self.color} {self.name}")
    def cost(self,price):
        if price> 50000:
            print(f"wow your {self.color} {self.name} is very costly")
        else:
            print(f"wow your {self.color} {self.name} is reasonable and very cool")


car1 = car("lambo","v12","blue" ,2010)
car2 = car("ferari" , "v16" , "green" ,2005 ) ## when using the function you must
### define evry single atribute and give it a specific input or else the program wont run
### print(car1)   ### this output will give the memory location of the  object not the atributes 


print(car1.color) ### the . operator will unpack the object and will output the atributes accordingly 
print(car1.year)
print(car1.engine_type)
print(car2.engine_type)
print(car2.speed(23))
print(car1.speed(67))
print(car1.is_driving())
print(car2.is_drinking())
print(car1.cost(12345))
print(car2.cost(100000))




### class variables 
### are shared among all instances(objects) of a class
### class variables defined outside the cunstructer
### instance variables defined inside the constructor (means before the def__init__)
### allows you to use them among all objects  through out the whole class 
### object variable syntax = self.variable =
### class variable syntax = class.variable = 
class student:
    num_students=0 ### class variable
    def __init__(self ,name,age,height ):
        self.name=name ### object variables
        self.age = age
        self.height = height
        student.num_students+=1

student1=student("bob",24,"5ft7")
student2 =student("jack",23,"6ft3")
student3 = student("jake",19,"5ft4")
student4 = student("go",3,5)
print(student.num_students)
print(f"there are {student.num_students} students in this class ")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)


### inheritance 
### allows different  clases to adopt each others  atributes and methods 
### helps with reusability and extensability
class animals:
    num=0
    def __init__(self,name ):
        self.name = name
    def eat(self):
        print(f"the {self.name} is eating")
    def sleep(self):
        print(f"the{self.name} is sleeping")
    def is_alive(self):
        return True
    

class Dog(animals):
    def speak(self):
        print("woof")
class Cat(animals):
    def speak(self):
        print("meow")


dog = Dog("scooby doo")
cat= Cat("Garfield")
print(dog.name)
print(cat.name)
dog.speak()
cat.speak()
dog.eat()
cat.eat()
dog.sleep()
cat.sleep()
print(animals.num)



### mulitple inheritance = inherit from more thn 1 parent class C(a,b)
### multi level inheritance = inherit from a parent which inherits from another parent
class animal:                 ### this is both  multiple and multi level inheritance 
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f" {self.name} is eating")
    def sleep(self):
        print(f" {self.name} is sleeping")
class predator(animal):
    def hunt(self):
        print(f"i hunt down animals and eat them so tasty")
class prey(animal):
    def flee(self):
        print(f"i run away from {self.name}")

class Rabbit (prey):
    pass
class Hawk(predator):
    pass

class Fish(predator,prey):
    pass



rabit = Rabbit("joe")
fish = Fish("nemo")
hawk = Hawk("tony")
hawk.sleep()
fish.hunt()
fish.flee()




### OOP PRACTICE CHALLENGES
### Try to solve these below each comment!

# 1. CLASS vs INSTANCE VARIABLES
# Create a class "Employee". 
# - Give it a class variable "company_name" (all employees work at the same place).
# - Give it instance variables "name" and "salary".
# - Create two employees and print their info + the company name.

class Employee:
    company_name="google"
    def __init__(self,name , salary):
        self.name=name
        self.salary=salary
        print(f"my name is {self.name} ,i work in {Employee.company_name} , and i earn {self.salary}  dollars per month")

employee1=Employee("joe" , 1000)
employee2=Employee("Jack" , 2000)




# 2. METHOD OVERRIDING
# Create a class "Electronic". Give it a method "power_on" that prints "System starting...".
# Create a child class "Laptop". 
# Override the "power_on" method so that for Laptops it prints "Laptop booting up..."
class Electronic:
    def power_on(self):
        print("system is starting up .....")
    
class Laptop(Electronic):
    def power_on(self):
        print("Laptop booting up...")


laptop = Laptop()
laptop.power_on()
# 3. MULTIPLE INHERITANCE
# Create a class "Camera" with a method "take_photo".
# Create a class "Phone" with a method "make_call".
# Create a class "SmartPhone" that inherits from BOTH and can do both actions.
class Camera:
    def take_photo(self):
        print("this device has taken a photo")

class Phone:
    def make_call(self):
        print("this device is now making a call")
    
class Smartphone(Camera,Phone):
    pass

smartphone = Smartphone()
smartphone.make_call()
smartphone.take_photo()



# 4. MULTI-LEVEL INHERITANCE
# Create a chain: Vehicle -> Car -> ElectricCar.
# - Vehicle should have a method "go".
# - Car should have a method "open_trunk".
# - ElectricCar should have a method "charge".
# Create an ElectricCar object and see if it can access all three methods.

class Vehicle:
    def go(self):
        print("this vehicle is driving")
    
class Car:
    def open_trunk(self):
        print("this cars trunk is opening")

class ElectricCar(Vehicle,Car):
    def charge(self):
        print("this vehicle is now charging")
        
vehicle = Vehicle()
car= Car()
electriccar = ElectricCar()
electriccar.go()
electriccar.open_trunk()
electriccar.charge()



### super() = Function used in child class to call methods from a parent class (superclass)
### adv = extends functionality and reusability of methods across different types of clases

class Shape:
    def __init__(self ,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    def describe(self):
        print(f"the shape is {self.color} in color ")
        print(f"is the shape filled up ? {self.is_filled}")
    def __str__(self):
        return str(vars(self))
       
import math 
class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        self.radius=radius
        super().__init__(color,is_filled)
    def __str__(self):
        return str(vars(self))
    def area(self):
        print(f"this circle has an area of {self.radius*self.radius*math.pi:.2f}cm^2 ")
    def perimeter(self):
        print(f"the perimeter of the circle is {self.radius*math.pi*2:.2f}cm")
    def describe(self):
        print("i have no edges")
        super().describe()  ### i can call the old desribe method from the parent class 
        ### as well as create a new describe method that will execute in the child class
class Square(Shape):
    def __init__(self,color,is_filled,length):
        self.length=length
        super().__init__(color,is_filled)
    def __str__(self):
        return str(vars(self))
    def area(self):
        print(f"the area of this square is {self.length*self.length}cm^2")
    def perimeter(self):
        print(f"the perimeter of this square is {4*self.length}cm")


class Triangle(Shape):
    def __init__(self,color,is_filled,length,height):
        self.height = height
        self.length = length
        super().__init__(color,is_filled)
    def __str__(self):
        return str(vars(self))
    def area(self):
        print(f"the area of this triangle is {0.5*self.length*self.height}cm^2")
    


circle = Circle("blue",True,5)
triangle = Triangle("grenn",False,5,10)
square = Square("pink",True,9)
square.describe()
triangle.describe()
print(circle,square,triangle, sep = "\n")
circle.area()
circle.perimeter()
triangle.area()
square.area()
square.perimeter()
circle.area()
circle.describe() ### if i define a new method in the child class it will overide 
### the old method defined in the parent class . this is called method overriding 




### conclusion
###  the self function allows us to define a parent class that has all the 
### common atributes that the children clases have so we dont need to define the logic again
###  we can simply  reuse that code 
### the __str__ method prints all the methods out as a string



# 5. THE CHALLENGE: THE super() KEYWORD
# Research or try to guess: How do you use the super() function?
# Create a parent "Person" that takes a "name" in its __init__.
# Create a child "Student" that takes "name" AND "grade".
# Use super().__init__(name) inside the Student to let the parent handle the name!

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    def __str__(self):
        return str(vars(self))

student1 = Student("bob", 9)
print(f"Student Check: {student1}")

print("\n" + "="*30 + "\n")

### BOSS-LEVEL OOP CHALLENGES

# 1. THE LOCKED VAULT (Encapsulation)
# - Create a class "BankAccount".
# - Make the "balance" attribute PRIVATE (use two underscores: self.__balance).
# - Create a method "deposit" to add money.
# - Create a method "get_balance" to see the money.
# - CHALLENGE: Try to print "account.__balance" from outside the class. What happens?

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"${amount} dollars has been deposited in your account.")

    def get_balance(self):
        print(f"You have ${self.__balance} in your account.")

# Create an instance (MUST use parentheses!)
account = BankAccount(100)
account.deposit(50)
account.get_balance()
