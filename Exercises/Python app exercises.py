### Greeting user

user_name = str(input("enter a name"))
def greet_user(user_name):
    if user_name!="":
        print(f"welcome {user_name}, ready to start your fitness journey")
    else:
        print("please enter a valid input")

### calories calculator
activity = str(input("Enter what activity you have performed today?(running/walking,etc)"))
speed = float(input("Enter the speed of which you have ran,walked or cycled (IN KMPH)"))
weight = float(input("please enter your weight (IN KG)"))
duration = float(input("please enter the amount of time you have performed this activity (IN HOURS)"))

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

# --- Running the program ---
print(calories_burned(activity, speed, weight, duration))

### BMI calculator
weight =float(input(("please enter your weight(lbs/kgs)")))
height = float(input("please enter your weight (ft/meters)"))
w_units = str(input("enter the units of measure you have inputed your weight in (kilos or pounds)"))
h_units = str(input("enter the units of measure you have inputed your height in(meters or inches)"))
bmi = 0
def calculate_BMI(weight,height ,w_units,h_units):
    if w_units=="lbs" and h_units=="inches":
        bmi = weight/(height**2)*703
        return bmi
    elif w_units=="kgs" and h_units=="meters":
        bmi = (weight/(height**2))
        return bmi
    else:
        return False
bmi = 
if bmi<18.5:
    print("you are underweight")
elif 18.5<=bmi<=25:
    print("you are perfectly healthy")
elif bmi>25:
    print("you are overweight please consider loosing some weight")
else:
    print("EROR")

### testing the program

print(calculate_BMI(weight,height ,w_units,h_units))














        
        
 







