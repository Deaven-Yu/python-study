age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

age = int(input("How old are you?"))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")    
number = int(input("Enter a number:"))
if number > 10:
    print("Big")
else:
    print("Small")   
current_weight = float(input("What is your current_weight?"))
target_weight = float(input("What is your target_weight?"))
if current_weight > target_weight:
    difference = current_weight - target_weight
    print(f"You still need to lose {difference}kg.")
elif current_weight < target_weight:
    difference = target_weight - current_weight
    print(f"You are {difference}kg below your target weight.")
else:
    print("You have reached your target weight")
x = 10
print(x > 5)
print(x == 10)
print(x != 10)
age = 18
if age > 18:
    print("A")
else:
    print("B")