wmax = 0
list = []
with open("text.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
    for i in a:
        wmax = max(len(i), wmax)
    for i in a:
        if len(i) == wmax:
            list.append(i)
    if len(a[-1]) + 1 == wmax:
        list.append(a[-1])
for i in list:
    print(i)

