table = [2 ** x for x in range(10) if x%2 == 0 ]
print(table)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

numbers = [1,2,'r',4]
strings = ["a","b","c"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[2]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

