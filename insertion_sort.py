a = [6,5,3,1,8,7,2,4,0]
count = 0

for i in range (1, len(a)):
    key = a[i]
    j = i-1
    #print ("before while",i,j)
    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j -= 1
        count += 1
        #print ("in while",i,j)
    a[j+1] = key
print("number of iterations performed ",count)
print(a)
