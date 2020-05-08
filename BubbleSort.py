a = [8,4,1,3,2,6]
count = 0
for i in range(len(a)):
    for j in range(1, len(a)):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            count += 1
print(a)
print(count)
