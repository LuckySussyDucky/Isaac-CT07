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

maximum = max(numbers2)
minimum = min(numbers2)
sum = sum(numbers2)
average = sum / len(numbers2)
print(maximum)
print(minimum)
print(sum)
print(int(average))


# Task 4a 

namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
            "Sophia", "Lucas", "Mia", "Aiden"
            ]
heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166
              ]
maximum = max(heightlist)
counter = heightlist.index(maximum)
name = namelist[counter]
print(maximum)
print(counter)
print(name)


# Task 4b

minimum = min(heightlist)
counter