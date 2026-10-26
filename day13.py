import weight_tools
change = weight_tools .calculate_change(76.2,75.5)

print(change)
print(weight_tools.get_trend(change))

from weight_tools import calculate_change,get_trend

change = calculate_change(80,78.5)

print(change)
print(get_trend(change))

import math
import random
import weight_tools as wt
print(math.sqrt(81))
print(random.randint(1,5))
change = wt.calculate_change(80,78.6)
print(change)
print(wt.get_trend(change))