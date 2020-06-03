a = [6,5,3,1,8,7,2,4,0]
count = 0
for i in range(len(a)):
    for j in range(1, len(a)):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            count += 1
print("number of iterations performed ",count)
print(a)