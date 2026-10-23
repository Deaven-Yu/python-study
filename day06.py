weights = [77.5,76.8,76.2,75.6]
print(weights)
print(type(weights))
print(weights[0])
print(weights[2])
weights[0]=77
print(weights)
weights.append(75.1)
print(weights)
target_weight = 71
weights = [77.5,72,71.5,70]
for weight in weights:
    if weight <= target_weight:
        print(f"{weight}kg reached!")

weights = [77.5,76.8,76.2,75.6,75.1]
lowest_weight = weights[0]
for weight in weights:
    if weight < lowest_weight:
        lowest_weight = weight
print(lowest_weight)