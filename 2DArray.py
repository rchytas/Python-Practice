from array import *

T = [
		[11, 12, 5, 2], 
		[15, 6,10], 
		[10, 8, 12, 5], 
		[12,15,8,6]
	]

#print(T[0])

#print(T[1][2])

#Inserting Values in Two Dimensional Array
T.insert(2, [0,5,11,13,6])

#for r in T:
#   for c in r:
        #print(c,end = " ")
    #print()

#Updating Values in Two Dimensional Array
T[2] = [11,9]
T[0][3] = 7
#for r in T:
    #for c in r:
        #print(c,end = " ")
    #print()

#Deleting the Values in Two Dimensional Array
del T[3]

for r in T:
    for c in r:
        print(c,end = " ")
    print()
