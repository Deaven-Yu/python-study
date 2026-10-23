with open("hello.txt","w",encoding="utf-8") as file:
    file.write("Hello,Deaven!")

with open("hello.txt","r",encoding="utf-8") as file:
    content = file.read()
print(content)

with open("hello.txt","w",encoding="utf-8") as file:
    file.write("First")

with open("hello.txt","a",encoding="utf-8") as file:
    file.write("\nSecond")


with open("notes.txt","w",encoding="utf-8") as file:
    file.write("Python Day10")

with open("notes.txt","a",encoding="utf-8") as file:
    file.write("\nFile handling is interesting.")

with open("notes.txt","r",encoding="utf-8") as file:
    content = file .read()
print(content)

date = input("Date:")
weight = float(input("Weight:"))
with open("weight_history.txt","a",encoding="utf-8") as file:
    file.write(f"{date},{weight}\n")
weight_records = []
with open("weight_history.txt","r",encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(",")
        date = parts[0]
        weight = float(parts[1])
        record = {
            "date":date,
            "weight":weight
        }
        weight_records.append(record)
print(weight_records)
def calculate_average(records):
    total = 0

    for record in records:
        total += record["weight"]

    average = round(total / len(records),2)
    return average
def find_lowest_weight(records):
    lowest_weight = records[0]["weight"]
    for record in records:
        if record["weight"] < lowest_weight:
            lowest_weight =record["weight"]
    return lowest_weight
def calculate_change(first_weight,last_weight):
    change = last_weight - first_weight
    return round(change,2)
first_weight = weight_records[0]["weight"]
last_weight = weight_records[len(weight_records) - 1]["weight"]
change = calculate_change(first_weight, last_weight)
def get_trend(change):
    if change < 0:
        return "Down"
    elif change > 0:
        return "Up"
    else:
        return "Stable"
trend =get_trend(change)
average = calculate_average(weight_records)
lowest_weight = find_lowest_weight(weight_records)

print(f"Average weight: {average}kg")
print(f"Lowest weight: {lowest_weight}kg")
print(f"Change: {change}kg")
print(f"Trend: {trend}")