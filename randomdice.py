import random

def twodice(numtimes):
    total = 0
    i = 0
    for i in range(numtimes):
        total = total + random.randint(1, 6)
    print(total)


twodice(1000)