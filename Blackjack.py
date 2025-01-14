import random

kortlek = [värde for värde in range(1, 14) for _ in range(4)]
random.shuffle(kortlek)

draget_kort = kortlek.pop()

print(f"Draget kort: {draget_kort}")