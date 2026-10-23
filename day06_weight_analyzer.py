weights = [77.5,76.8,76.2,75.6,75.1]
total = 0
for weight in weights:
    total +=weight
average =    total / len(weights)
print(round(average,2))
lowest_weight=weights[0]
for weight in weights:
    if weight < lowest_weight:
        lowest_weight = weight
print(lowest_weight)
count = 0
for weight in weights:
    if weight <76:
        count += 1
print(count)