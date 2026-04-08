### calculator program 
num1=float(input("enter a number"))
num2 =float(input("enter a number"))
operand = str(input("Enter operand"))
n=int(input("the power you want to raise your number too "))
import math 

if operand == "+":
    sum = num1+num2
    print(sum)
elif operand == "-":
    difference = num2-num1
    print(difference)
elif operand == "*":
    prod = num1*num2
    print(prod)
elif operand == "/":
    divi = num2/num1
    print(divi)
elif operand == "**1":
    result1 = math.pow(num1 ,n)
    print(result1)
elif operand == "**2":
    result2 = math.pow(num2 ,n)
    print(result2)
elif operand == "**":
    result = num1**num2
    print(result)
else:
    print("this is an invalid opearation that this calculator doesnt suport")




    ### Weight converter program to convert kilos to pounds 
weight_measurement = str(input("enter the measurement you will be giving your weight in:"))
weight1 = float(input("enter your weight  "))
if weight_measurement == "kgs":
    new_weight1 = weight1*2.205
    print(new_weight1)
elif weight_measurement == "lbs":
    new_weight2 = weight1/2.205
    print(round(new_weight2,2))
else:
    print(" Eror , invalid unit ")



### Temperature conversion program (convert all to celcius )
unit = str(input("enter a unit of temperature "))
temp = float(input("enter the temperature "))
if unit =="kelvin":
    temp = temp -273
    print(temp)
elif unit == "F":
    temp = (temp-32)*(5/9)
    print(round(temp,2))
elif unit == "C":
    print(temp)
else:
    print("invalid unit of temp")




#i = int(input("enter a level"))
while i>0:
    if i>=4:
    print("this level does not exist please input again ")

j = int(input("enter "))



user_input = int(input("enter a number"))
### number of rows = number of number present in the grid

for i in range(1,user_input+1): 
    for j in range (1,i+1):
        if j %2 == 0:
            print("E" , sep = "")
        else:
            print(j , end = "")
print()





