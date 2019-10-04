##!/usr/bin/env python3
from random import uniform
from statistics import stdev, mean

def throw_Needles(n):
    global pi_list
    for i in range(100):
        hit = 0
        for _ in range(n):
            if (uniform(-1,1)**2 + uniform(-1,1)**2) <= 1:
                hit += 1
        aprox_pi = float(hit / n)
        aprox_pi *= 4
        pi_list[i] = aprox_pi

    global average
    deviation = stdev(pi_list)
    return deviation

pi_list = []
for _ in range(100):
    pi_list.append(0)
average = 0
needle_number = 500
deviation = 1

while (deviation >= 0.005):
    needle_number += needle_number
    deviation = throw_Needles(needle_number)
    print("Another one: ", needle_number, "   Deviation:", deviation)

average = mean(pi_list)
print("Needles per estimation: ", needle_number)
print("Pi average: ", average)
print("Pi deviation: ", deviation)