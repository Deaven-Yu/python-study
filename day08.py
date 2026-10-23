record_count = int(input("请输入计数次数："))
weight_records = []
for number in range(record_count):
    date = input(f"请输入第{number + 1}次日期：")
    weight = float(input(f"请输入第{number + 1}次体重："))

    record ={
            "date" : date,
            "weight" : weight
        }
    weight_records.append(record)
   
print(weight_records)
for record in weight_records:
    print(f"{record["date"]}:{record["weight"]}kg")
total = 0
for record in weight_records:
    total += record["weight"]
average = round(total / len(weight_records),2)
print(f"Average weight:{average}kg")
lowest_weight = weight_records[0]["weight"]
for record in weight_records :
    if record["weight"]< lowest_weight:
        lowest_weight = record["weight"]
print(f"Lowest_weight:{lowest_weight}kg")
first_weight = weight_records[0]["weight"]
last_weight = weight_records[len(weight_records)-1]["weight"]
change = last_weight - first_weight
change = round(change,2)
print(f"change:{change}kg")
if change < 0:
    print("Trend:Down")
elif change > 0:
    print("Trend:Up")
else:
    print("Trend:Stable")
