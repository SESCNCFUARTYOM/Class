list = [1, 2, 3, 4, 8, 2, 3, 1]

print(len(set(list)))

for i in set(list):
    count = 0

    for j in list:
        if j == i:
            count+=1
    print(f"{i} Входит: {count}")

