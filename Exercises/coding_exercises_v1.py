### the fizz bizz
for i in range(1,101):
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("bizz")
    elif i%3==0 and i%5==0:
        print("fizzbizz")
    else:
        print(i)


### Matrix builder
user_input=int(input("enter the number you want ur matrix to be build upon"))
for rows in range(user_input):
    for columns in range(user_input):
        print(columns , end ="")
    print()



### shoping cart program
foods = []
total =0
prices = []
while True:
   food = str(input("what would you like to purchase today (press q to quit)"))
   if food =="q":
        break
   else:
    price=float(input("enter the price of the food")) 
    foods.append(food)
    prices.append(price)
    total = sum(price)









            

