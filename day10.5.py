with open("weight_history.txt","r",encoding="utf-8") as file:
    content = file.read()
print(type(content))
print(content)
line = "10-20,75.2\n"
parts = line.strip().split(",")
print(parts)
print(type(parts))
print(type(parts[0]))
print(type(parts[1]))
print(float(parts[1]) - 1)