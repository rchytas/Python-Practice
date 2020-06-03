a = (1,2,3,4,5,6)
print(type(a))

for i in range (len(a)):
	print (a[i]**2)

b = [7,8,9,10]

c = tuple(b)

print (c)

marks = {'Alex': 45, 'Bob': 48, 'Chef': 87}

print(marks)

marks['Alex'] = 90

print("After updating dict ",marks)

marks['Tom'] = 100

print("After adding dict ",marks)

del marks['Alex']

print("After deleting dict ",marks)

print("Check out another dict")

x = {4:"hi", "yo":56, 34:12}

for key in x:
	print(key," ",x[key])

y = x.copy()

print("Copied above dict to new dict called y")

print(y)

items = marks.items()

print("now got the items from dict",items)

values = marks.values();

print("now got the values from dict",values)

mykeys = marks.keys()

print("now got the keys from dict",mykeys)

marks.clear()

print("now cleared the dict",marks)


a = {1:2, 3:4}

b = {3:5, 7:9}

print(a)
print(b)

a.update(b)

print("Update function on two above dict")

print(a)