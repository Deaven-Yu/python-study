person = {"name":"Deaven",
          "age":20,
          "height":179,
          "current_weight":75.6,
          "target_weight":71
}
person["bmi"] = 23.7
person["exercise_days"] = 3
person["goal"] = "lose fat"
print(f"我的名字是:{person['name']}")
print(f"我的年龄是:{person['age']}")
print(f"我的当前体重是{person['current_weight']}kg")
print(f"我的目标体重是{person['target_weight']}kg")
print(f"我的BMI是:{person['bmi']}")
print(f"我每周训练:{person['exercise_days']}次")
print(f"我的目标是:{person["goal"]}")
student = {
    "name":"Deaven",
    "score":80
}
print(student["score"])
student["score"] = 95
print(student["score"])

person = {
    "name":"Deaven"
}
person["bmi"] = 23.7
print(person)

weight_records = [
    {
        "date":"9-20",
        "weight":76.8
    },
    {
        "date":"9-21",
        "weight":76.2
    },
    {
        "date":"9-22",
        "weight":75.6
    }
]
print(f"{weight_records[0]['weight']}")
print(f"{weight_records[1]['weight']}")
print(f"{weight_records[2]['date']}")

for record in weight_records:
    print(f"{record['date']}:{record['weight']}kg")
