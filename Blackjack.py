import random

kortlek = (list(range(1, 14)) * 4) * 6
random.shuffle(kortlek)

draget_kort = kortlek.pop()
print("Draget kort:",draget_kort)