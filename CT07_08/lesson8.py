print("Hello from lesson 8")

# Recap 1

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]
allNum = [
]
unique = [
]
allNum = list1 + list2 + list3
print(allNum)
for numbers in allNum:
    if numbers not in unique:
        unique.append(numbers)
unique = (sorted(unique))
index = len(unique) // 2
print(unique[:index])
print(unique[index:])
