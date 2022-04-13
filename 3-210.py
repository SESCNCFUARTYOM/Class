

a = list()
b = list()

a = input().split()
b = input().split()

c = list()

for i in a:
    c.append(i)
for j in b:
    c.append(j)


print(sorted(c))