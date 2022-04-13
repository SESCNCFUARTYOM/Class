a = [1,-2,3,4,-65,3,6,23,4,2]
sum = 0
count = 0
for i in a:
    if (i > 0):
       sum += i
    elif (i < 0):
        count += 1
print(sum, count)