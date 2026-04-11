#!/usr/bin/python2.7
import random
number = random.randint(-10, 10)

# Buradan etibarən sizin yazmalı olduğunuz kod başlayır
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
