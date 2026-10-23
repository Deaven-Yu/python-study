def say_hello():
    print("Hello,Deaven!")

say_hello()

def greet():
    print("Hello!")
    print("Welcome to python.")

greet()
greet()

def greet(name):
    print(f"Hello,{name}!")

greet("Deaven")

def add(a,b):
    result = a + b
    return result

answer = add(2,3)
print(answer)
def show_record(date,weight):
    print(f"{date}:{weight}kg")
show_record("10-15",75.5)
def calculate_change(first_weight,last_weight):
    change = last_weight - first_weight
    change = round(change,2)
    return change
def get_trend(change):
    if change < 0:
        return "Down"
    elif change > 0:
        return "Up"
    else:
        return "Stable"
print(get_trend(-1.6))
print(get_trend(0.8))
print(get_trend(0))

change = calculate_change(76.2,75.5)
print(change)
result = calculate_change(80,78.4)
print(result)

def calculate_average(records):
    total = 0
    for record in records:
        total += record["weight"]
    average = round(total/len(records),2)
    return average

weight_records = [
    {"date": "10-12", "weight": 76.2},
    {"date": "10-13", "weight": 75.8},
    {"date": "10-14", "weight": 75.5}
]

average = calculate_average(weight_records)