tableOf = input ("Enter Number of tables you want: ")
for i in range(1,int(tableOf)+1):
	for x in range(1,11):
		print (i * x, end = " ")
		#print (i * x)
	print()