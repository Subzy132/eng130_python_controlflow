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
elif age >= 16 and age <= 17:
    print("you are eligible for 16+ movies")
elif age == 15:
    print("you are eligible for 15+ films")
elif age >= 12 and age <= 14:
    print("you are eligible to watch 12a but may need an adult supervision ")
elif age >= 0 and age <= 4:
    print("you will need parental guidance to watch this film")
elif age >= 5 and age <= 11:
    print("This film is universal")
else:
    print("please enter your age again")

