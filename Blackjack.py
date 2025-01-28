import random

kortlek = (list(range(1, 14)) * 4) * 6
random.shuffle(kortlek)

spelarens_kort = [kortlek.pop(), kortlek.pop()]
dator_kort_synligt = kortlek.pop()
dator_kort_hemligt = kortlek.pop()

print("Spelarens kort:", spelarens_kort)
print("Datorns kort:", dator_kort_synligt)