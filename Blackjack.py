import random

kortlek = (list(range(1, 14)) * 4) * 6
random.shuffle(kortlek)

spelarens_kort = [kortlek.pop(), kortlek.pop()]
datorns_kort = kortlek.pop()

print("Spelarens kort:", spelarens_kort)
print("Datorns kort:", datorns_kort)