le = int(input())
re = int(input())
pe = int(input())
te = int(input())

if (0 > le or 100 < le or 0 > re or 100 < re or 0 > pe or 100 < pe or 0 > te or 100 < te):
    print("Input error")
elif (40 > pe or 40 > te):
    print("RFC")
else:
    print(int((le + re + 4 * pe + 4 * te) / 50))
