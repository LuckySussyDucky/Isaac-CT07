print("Hello from lesson 7")

# Task 1

fruits1 = ["Apple", "Banana", "Cherry"]
fruits2 = ["Durian", "Elderberry", "Figs"]
fruits = [
]
fruits = fruits1 + fruits2
print(fruits)


# Task 2

price1 = [3.20, 2.65, 1.75]
price2 = [6.15, 5.45, 4.20]
price = [
]
price = price1 + price2
print(sorted(price))


# Task 3

fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
fruit1 = [
]
fruit2 = [
]
index = 3
print(fruits[0:index])
print(fruits[index:6])


# Task 4

lenH = len(fruits) // 2
print(fruits[:lenH])
print(fruits[lenH:])


# # Extra 1

# students = [
# ]
# student1 = ["john", "88460638", "john.yeo@gmail.com"
# ]
# student2 = ["jared", "80584155", "jared.pak@gmail.com"
# ]
# student3 = ["zhi wei", "97426101", "tan.zhiwei@gmail.com"
# ]
# student1.append()

# Task 5

fruit1 = ["Apple", "Banana", "Cherry", "Durian"]
fruit2 = ["Cherry", "Durian", "Elderberry", "Figs"] 
commonFruits = [
]
for fruit in fruit1:
    for fruits in fruit2:
        if fruit == fruits:
            commonFruits.append(fruit)
print(commonFruits)


# Task 6

fruit1 = ["Apple", "Banana", "Cherry", "Cherry"]
fruit2 = ["Cherry", "Durian", "Durian", "Figs"]
allFruits = [
]
unique = [
]
allFruits = fruit1 + fruit2
for fruit in allFruits:
    if fruit not in unique:
        unique.append(fruit)
print(unique)


# Task 7

num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]
allNum = [
]
allNum = 
