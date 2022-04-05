a = list()
wmax = 0
count = 0
while True:
    i = float(input())
    if i == 0:
        break
    else:
        a.append(i)
for i in a:
    wmax = max(i, wmax)
for i in a:
    if i == wmax:
        count += 1
print(wmax, count)