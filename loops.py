list_data = [1, 2, 3, 4, 5]

for i in list_data:
    if i == 3:
        print(i)
    elif i > 3:
        print("you have passed 3")
    else:
        print("too soon")

student_1 = {
    "name": "Subhaan",
    "course_name": "Devops",
    "completed_lessons": 4,
    "completed_lessons_names" : ["lists", "tuples", "strings"]
}

for key in student_1:
    print(key, "->", student_1[key])

data = 0

while data < 10:
    print(f"it's working -> {data}")
    if data == 5:
        break
    data += 1

user_prompt = True

while user_prompt:
    age = input('please enter your age: ')
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits only")

print(f"your age is {age}")