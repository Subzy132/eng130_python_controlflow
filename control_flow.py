# If it's cold
#   take jacket
# If it's raining
#   take rain mack
# If it's sunny: boolean value true - next line
#   let's go to the beach
# else or elif

weather = "raining"

if weather == "cold": # True or False
    print("Wear a jacket!") # If true this will be executed
elif weather == "sunny":
    print("let's go to the beach!")
elif weather == "raining":
    print("wear a rain mack")
else:
    print("No match! Better luck next time")

age = int(input("Enter your age: "))

if age >= 100:
    print("Please enter an age below 100!")
elif age >= 18:
    print("you are eligible for 18+ movies")
elif age
