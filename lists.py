thislist = ["apple", "banana", "cherry"]
print(thislist)

mylist =["vedant", "omm", "mayur"]
print(mylist)

print(len(mylist)) #length of list

print(mylist[0])

print(mylist[-1])

mylist[1] = "rahul"
print(mylist)

mylist.append("akash")
print(mylist)

mylist.insert(1, "rohit")
print(mylist)

mylist.extend(["ajay", "karan"])
print(mylist)

mylist.remove("omm")
print(mylist)

mylist.pop()
print(mylist)

mylist.pop(1)
print(mylist)

del mylist[1]
print(mylist)

mylist.clear()
print(mylist)

print("vedant" in mylist)

print("sachin" not in mylist)

print(mylist.index("omm"))

mylist.reverse()
print(mylist)

newlist = mylist.copy()

print(newlist)

friends = ["rohit", "akash"]

newlist = mylist + friends

print(newlist)

print(mylist * 2)

print(mylist[0:2])

print(mylist[1:])

print(mylist[::-1])

for name in mylist:
    print(name)

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #constructor

mylist = ["apple", "banana", "cherry"]
print(type(mylist))