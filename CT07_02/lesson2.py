print("Hello from lesson 2")


# Task 1

for i in range(0,21):
    print(i)

for i in range(1,31):
    print(i)

for i in range(2,25,2):
    print(i)


# Task 2

counter = 0
while counter < 21:
    print(counter)
    counter += 1

counter = 1
while counter < 31:
    print(counter)
    counter += 1

counter = 2
while counter < 25:
    print(counter)
    counter += 2


# Task 3

counter = 1
while True:
    print(counter)
    counter += 1
    if counter == 6:
        break


# Task 4a

counter = 1
while True:
    print(counter)
    counter += 1
    if counter == 11:
        break
print("YAY")


# Task 4b

counter = 1
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 6:
        break
else:
    print("YAY")


# Task 5

toppings = input("What toppings would you like on your pizza? ")
while True:
    toppings2 = input("What other toppings would you like on your pizza? ")
    if toppings2 == "end":
        break
    else:
        stuff = "toppings" + ""