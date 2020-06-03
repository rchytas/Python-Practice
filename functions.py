def greet(name, action):
    print("hello",name, "Good Morning")
    print ("do", action)

def greet1(*name):
    for my_name in name:
        print("hello",my_name, "Good Evening!")

def simple_interest(p,r,t):
    si = (p * r * t) / 100
    return si

def infinite(count):
    if (count == 0):
        return
    print("Infinite", count)
    count -= 1
    infinite(count)

# Factorial of a number n
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# Demonstrates Binary Search Algorithm
def binary_search (input_arr, key, start, end):
    print("Binary Search Results")

    if start <= end:
        mid = int((start + end) / 2)
        if input_arr[mid] > key:
            return binary_search (input_arr, key, start, mid-1)
        elif input_arr[mid] < key:
            return binary_search (input_arr, key, mid+1, end)
        else:
            return mid
    else:
        print("Can't find the requested element in the array")
        return -1
    
# Demonstrates Insertion Sort Algorithm
# [1,4,2,6,1,0,8]
def insertion_sort(a):
    print("Original Array",a)
    print("Insertion Sort Results")
    for i in range (1, len(a)):
        key = a[i]
        j = i-1
        print("Now checking Indexes ",i,j)
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    print(a)

# Demonstrates Bubble Sort Algorithm
def bubble_sort(a):
    print("Bubble Sort Results")
    for i in range(len(a)):
        for j in range(1, len(a)):
            print("Now checking Indexes ",i,j)
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    print(a)

# Demonstrates Fibonacci Series using recursion
def fibonacci(i):
    if i < 2:
        return i
    else:
        return (fibonacci(i-1) + fibonacci(i-2))

# Optimized version of fibonacci series for n terms
# To get particular number k in the series do fibs(n)[k]
def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    res =""
    for char in str:
        if ord(char) >=65 and ord(char) <= 90:
            res +=chr(ord(char)+32)
        else:
            res+=char
    
    return res