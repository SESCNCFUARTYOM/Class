wmax = 0
with open("text.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
    for i in a:
        wmax = max(len(i), wmax)
    for i in range(1, wmax + 1):
        for j in a:
            if len(j) == i:
                print(j)


