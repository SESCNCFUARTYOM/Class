a = [1, 2, 3, 4, 5, 2]
for i in range(1, len(a)):
    if a[i] >= a[i-1]:
        continue
    else:
        print("Error")
