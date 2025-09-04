# Create a set

s = set()
#add some elements to the set

s.add(1)
s.add(2)
s.add(3)
s.add(4)

name = int(input("Type a number 1-4: "))
if name == 1:
    s.remove(1)
    print(s)
elif name == 2:
    s.remove(2)
    print(s) 
elif name == 3:
    s.remove(3)
    print(s) 
elif name == 4:
    s.remove(4)
    print(s) 
    