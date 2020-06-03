a = []

def enqueue(element):
    a.append(element)

def dequeue():
    if len(a) <= 0:
        print("Your Queue is Empty")
    else:
        return a.pop(0)

def display_queue():
    for i in range (len(a)-1,-1,-1):
        print(a[i], end = " ")
    print()
    

enqueue(24)
enqueue(2)
display_queue()
print("Now Removing")
dequeue()
display_queue()
enqueue(43)
display_queue()
enqueue(1)
display_queue()
print("Now Removing")
dequeue()
display_queue()
enqueue(12)
display_queue()
