import time

print (2**5)

n = 10000
start = time.time()
sum = 0
for i in range (1,n+1):
    sum += i
end = time.time()
print (sum)

print (end - start, 'time taken using for loop for first 10,000 numbers')

start = time.time()
sum = (n* (n+1))/2
print (sum)
end = time.time()	
print (end - start, 'time taken using the fomula for first 10,000 numbers')

