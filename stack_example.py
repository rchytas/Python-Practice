a = []

def push_in_stack(element):
    a.append(element)

def pop_from_stack():
    if len(a) <= 0:
        print("Your Stack is Empty")
    else:
        return a.pop()

def display_stack():
    for i in range (len(a)-1,-1,-1):
        print(a[i], end = " ")
    print()
    

push_in_stack(24)
push_in_stack(2)
display_stack()
print("Now Removing")
pop_from_stack()
display_stack()
push_in_stack(43)
display_stack()
push_in_stack(1)
display_stack()
print("Now Removing")
pop_from_stack()
display_stack()
push_in_stack(12)
display_stack()
