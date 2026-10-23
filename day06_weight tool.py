count = int(input("请输入记录次数："))
weights =[]
for number in range(count):
    weight=float(input("请输入体重："))
    weights.append(weight)
print(weights)
total= 0
for weight in weights:
    total +=weight
average = round(total / len(weights),2)
print(f"平均体重：{average}kg")
lowest_weight = weights[0]
for weight in weights:
    if weight < lowest_weight:
        lowest_weight = weight
print(f"最低体重：{lowest_weight}kg")
success_count = 0
for weight in weights:
    if weight <76:
        success_count +=1
print(f"低于76kg次数:{success_count}次")