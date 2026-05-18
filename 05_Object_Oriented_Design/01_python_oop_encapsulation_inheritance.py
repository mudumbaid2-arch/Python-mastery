

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




### FITNESS APP OOP CHALLENGES 🏋️‍♂️

# 1. THE PRIVATE PROFILE (Encapsulation)
# - Create a class "User".
# - Make "weight" a PRIVATE attribute (self.__weight).
# - Create a method "update_weight(self, new_weight)" that only updates it if the weight is positive.
# - Create a method "get_weight(self)" to return the weight.


# 2. EXERCISE TYPES (Inheritance)
# - Create a parent class "Exercise" with attributes "name" and "duration".
# - Create a child class "Cardio" that adds an "avg_heart_rate" attribute.
# - Create a child class "Strength" that adds "sets" and "reps" attributes.
# - Use super().__init__ in both child classes!
class Exercise:
    def __init__(self,name,duration):
        self.name=name
        self.duration=duration
class Cardio(Exercise):
    def __init__(self,name,duration,avg_heartbeat):
        super().__init__(name,duration)
        self.avg_heartbeat=avg_heartbeat
   
class Strength(Exercise):
    def __init__(self,name,sets,reps,duration):
        self.sets=sets
        self.reps=reps
        super().__init__(name,duration)

exercise=Exercise("running",20)
cardio = Cardio("running",20,170)
strength=Strength("bench press",3,12,15)
print(cardio.avg_heartbeat)
print(strength.name)


### 3. THE WORKOUT LOG (Composition)
### - Create a class "WorkoutSession".
# - It should have a date and an empty list called "exercise_list".
# - Create a method "add_exercise(self, exercise)" that adds an Exercise object to the list.
# - Create a method "summary(self)" that prints the name of every exercise in that session.
class Workoutsession:
    def __init__(self):
        self.lst = []

    def date(self):
        year=2026
        for i in range(1,13):
            if i%2!=0:
                for j in range(1,32):
                    date = j,i ,year
                    print(date)
            elif i==2:
                for j in range(1,28):
                    date=j,2,year
                    print(date)
            elif i%2==0:
                for j in range(1,31):
                    date =j,i ,year
                    print(date)

    def add_exercise(self, *args):
        for ex in args:
            self.lst.append(ex)

    def summary(self):
        print(f"this is the list of excercises you have done in todays session: {self.lst}")

my_session = Workoutsession()
# my_session.date() # Commented this out so it doesn't print 365 lines!
my_session.add_exercise("bench")
my_session.summary()


# 4. CALORIE BURNER (Polymorphism / Overriding)
# - Add a method "calculate_calories(self)" to the "Exercise" class (returns 0 by default).
# - Override it in "Cardio" (formula: duration * 10).
# - Override it in "Strength" (formula: sets * reps * 2).
# - Create a Cardio and a Strength object, and print their calories!
