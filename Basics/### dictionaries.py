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



### arbitrary arguments means the fucntion wil allow a varying number of arguments
### *args = multiple arguments and **kwargs = multiple key word arguments
def add(*nums):  ### replace parameters with *args to accept N number of parameters
    total = 0
    print(type(args))
    for num in nums:
        total=total+arg
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







