import matplotlib.pyplot as plt
import numpy as np

'''
x = [1,4,7,9]
y = [2,45,12,48]


plt.plot(x, y,'r-.')
plt.plot(y,x)
plt.xlabel("Time")
plt.ylabel("Expenses")
plt.title("My First Graph")
plt.show()

x = [i for i in range(10)]
y = [i*i*i for i in range(10,20)]
z = [i*2 for i in range(10,20)]

plt.subplot(2,1,1)
plt.plot(x,y)
plt.subplot(2,1,2)
plt.plot(x,z)
plt.show()


# Sin and Quadratic Graphs
x = np.arange(-10, 10, 0.1)
#y = np.sin(x)
y= x*x + 2*x +5
plt.plot(x, y,'r-.')
#plt.title("Sin Graph")
plt.title("Quadratic Graph")
plt.show()


# Bar Charts
x = [i for i in range(10)]
y = [4,1,7,2,9,5,12,5,6,8]
x2 = [i+0.2 for i in range(10)]
z = [4,2,9,2,4,0,1,5,5,2]

plt.bar(x,y,color = "green", width = 0.2, label="2018")
plt.bar(x2,z,color = "red", width = 0.2, label="2019")
plt.legend()
plt.show()
'''

hours = [2,6,1,4,2,6,2,1]
explodes = [0.2,0,0,0,0.2,0,0,0.2]
activities= ["Ready","School","Rest","Study","Play","Sleep","TV","Yoga"]

plt.pie(hours,labels=activities, explode=explodes)
plt.show()

