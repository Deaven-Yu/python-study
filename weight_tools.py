def calculate_change(first_weight, last_weight):
    change = last_weight - first_weight
    return round(change, 2)


def get_trend(change):
    if change < 0:
        return "Down"
    elif change > 0:
        return "Up"
    else:
        return "Stable"

if __name__ == "__main__":
    print("Testing weight_tools...")
    print(calculate_change(80, 78.5))
    print(get_trend(-1.5))