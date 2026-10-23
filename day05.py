for number in range(1,6):
    number = number*2
    print(number)

total = 0
for number in range(1,11):
    total = total + number
print(total)

current_weight = 75
target_weight = 71
while current_weight > target_weight:
    print(f"Current_weight:{current_weight}kg")
    current_weight = current_weight - 1
print(f"Current_weight:{current_weight}kg")
print("Target reached!")
count = 1
while count <= 3:
    print(f"Before:{count}")
    count +=1
    print(f"After:{count}")

number = 1
total = 0
while number <=5:
    total +=number
    number +=1 
print(total)