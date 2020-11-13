import random

test_seed = int(input("Create a seed number:"))
random.seed(test_seed)

coinside = random.randint(0, 1)
if coinside == 1:
    print("Heads")
else:
    print("Tails")
