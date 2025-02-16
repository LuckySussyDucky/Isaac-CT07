import random
print("Hello from lesson 5")

# Task 1

numbers = [
]
counter = 100
while counter != 0:
    num = random.randint(1, 1000)
    numbers.append(num)
    counter = counter - 1
print(numbers)


# Task 2 

numbers2 = [
]
counter = 100
while counter != 0:
    num = random.randint(1, 1000)
    if num not in numbers:
        numbers2.append(num)
        counter = counter - 1
print(numbers)


# Task 3 

maxi