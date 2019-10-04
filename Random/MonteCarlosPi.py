import random


def throw_Float_Dart():
    if (random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2) <= 1:
        return 1
    else:
        return 0


def throw_Int_Dart():
    if (random.randint(-1, 1)**2 + random.randint(-1, 1)**2) <= 1:
        return 1
    else:
        return 0


total = 10000000
float_Hit = 0
int_Hit = 0

for _ in range(total):
    float_Hit += throw_Float_Dart()
    int_Hit += throw_Int_Dart()

float_Pi = float(float_Hit / total)
float_Pi *= 4

int_Pi = float(int_Hit / total)
int_Pi *= 4

print("Float Darts:\n" + str(float_Pi))
print("Int Darts:\n" + str(int_Pi))
