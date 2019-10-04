num = float(input())

aprox = num / 2.0

while(True):
    new_aprox = (aprox + num / aprox) / 2.0
    if (abs(new_aprox - aprox) < 0.01):
        break
    else:
        aprox = new_aprox

print("%.3f" % aprox)
