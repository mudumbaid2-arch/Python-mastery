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


# 3. THE WORKOUT LOG (Composition)
# - Create a class "WorkoutSession".
# - It should have a date and an empty list called "exercise_list".
# - Create a method "add_exercise(self, exercise)" that adds an Exercise object to the list.
# - Create a method "summary(self)" that prints the name of every exercise in that session.


# 4. CALORIE BURNER (Polymorphism / Overriding)
# - Add a method "calculate_calories(self)" to the "Exercise" class (returns 0 by default).
# - Override it in "Cardio" (formula: duration * 10).
# - Override it in "Strength" (formula: sets * reps * 2).
# - Create a Cardio and a Strength object, and print their calories!
