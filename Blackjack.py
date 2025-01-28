import random

kortlek = (list(range(1, 14)) * 4) * 6
random.shuffle(kortlek)

dragna_kort = [kortlek.pop(), kortlek.pop()]
print("Dragna kort:",dragna_kort)