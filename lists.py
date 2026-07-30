# ==========================================
# Python List - All Operations
# ==========================================

# 1. Create List
mylist = ["vedant", "omm", "mayur"]
print("1. Original List:", mylist)

# 2. Length of List
print("2. Length:", len(mylist))

# 3. Access Elements
print("3. First Element:", mylist[0])
print("4. Last Element:", mylist[-1])

# 4. Change Element
mylist[1] = "rahul"
print("5. After Updating:", mylist)

# 5. Append
mylist.append("akash")
print("6. After Append:", mylist)

# 6. Insert
mylist.insert(1, "rohit")
print("7. After Insert:", mylist)

# 7. Extend
mylist.extend(["ajay", "karan"])
print("8. After Extend:", mylist)

# 8. Remove
mylist.remove("rahul")
print("9. After Remove:", mylist)

# 9. Pop Last Element
mylist.pop()
print("10. After pop():", mylist)

# 10. Pop by Index
mylist.pop(1)
print("11. After pop(1):", mylist)

# 11. Membership Operators
print("12. Is 'vedant' Present?", "vedant" in mylist)
print("13. Is 'sachin' Not Present?", "sachin" not in mylist)

# 12. Index
print("14. Index of 'mayur':", mylist.index("mayur"))

# 13. Count
mylist.append("vedant")
print("15. Count of 'vedant':", mylist.count("vedant"))

# 14. Reverse
mylist.reverse()
print("16. Reversed List:", mylist)

# 15. Sort
mylist.sort()
print("17. Sorted List:", mylist)

# 16. Copy
newlist = mylist.copy()
print("18. Copied List:", newlist)

# 17. Concatenate Lists
friends = ["rohit", "akash"]
combined = mylist + friends
print("19. Combined List:", combined)

# 18. Repeat List
print("20. Repeated List:", mylist * 2)

# 19. Slicing
print("21. First Two Elements:", mylist[0:2])
print("22. From Index 1:", mylist[1:])
print("23. Reverse using Slicing:", mylist[::-1])

# 20. Loop
print("24. Loop through List:")
for name in mylist:
    print(name)

# 21. Enumerate
print("25. Enumerate:")
for index, name in enumerate(mylist):
    print(index, name)

# 22. List Comprehension
upper_names = [name.upper() for name in mylist]
print("26. Uppercase List:", upper_names)

# 23. Max and Min
print("27. Maximum:", max(mylist))
print("28. Minimum:", min(mylist))

# 24. Delete Element
del mylist[1]
print("29. After del:", mylist)

# 25. Clear List
mylist.clear()
print("30. After clear():", mylist)

# 26. Type
thislist = ["apple", "banana", "cherry"]
print("31. Type:", type(thislist))

# 27. Constructor
thislist = list(("apple", "banana", "cherry"))
print("32. Constructor List:", thislist)
print("33. Length of Constructor List:", len(thislist))