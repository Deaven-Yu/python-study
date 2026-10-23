weights = [77.5,76.8,76.2,75.6]
total =0
for weight in weights:
    total += weight
print(total)

number = 1
while number <= 5:
    print(number)
    number += 1

numbers = [1,2,3,4,5]
total = 0
for number in numbers:
    total += number
print(total)

current_weight = 75
target_weight = 71
while current_weight < target_weight:
    print(current_weight)
    current_weight = target_weight
print(current_weight)
print("Target reached!")

weights = [77.5,76.8,76.2,75.6,75.1]
highest_weight = weights[0]
for weight in weights:
    if highest_weight < weight:
        highest_weight = weight
print(highest_weight)

weight_records = [
    {"date":"9-20","weight":76.8},
    {"date":"9-21","weight":76.2},
    {"date":"9-22","weight":75.6}
]
for record in weight_records:
    print(f"{record["date"]}:{record["weight"]}kg")

current_weight = 75
target_weight = 71
while current_weight > target_weight:
    print(current_weight)
    current_weight -=1
print(current_weight)
print("Target reached!")