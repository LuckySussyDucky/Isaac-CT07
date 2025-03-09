import random
# Question 1

MonstersFought = 0
HeroHealth = 100
print("Hero starts on his adventure with Health:", HeroHealth)

while HeroHealth > 0:
    healthLost = random.randint(1, 15)
    HeroHealth = HeroHealth - healthLost
    print("After fighting a monster, his Health is now:", HeroHealth)
    MonstersFought = MonstersFought + 1
else:
    print("The Hero fought", MonstersFought, "battles, and died.")


# Question 2

Order = [
]
counter = 1
FoodToEat = "hi"
while FoodToEat != "end":
    FoodToEat = input("What would you like to eat? ")
    Order.append(FoodToEat)
print("You have the following order:")
Order.pop(len(Order)- 1)
for i in range(len(Order)):
    print(counter, ".", Order[i])
    counter = counter + 1





line = "ROBLOX,USD,0,813345,4.5,Games"
words = line.split(",")
print(words[1])
print(words[-1])
print(words[0])
print(words[3])
print(words[2])

correct = False
hiddenpwd = "computhink"

# Password validation
while not correct:
	userpwd = input("What is the password? ")

if userpwd == hiddenpwd:
	correct = True

print("Access granted")

import random
lucky_draw = []

while len(lucky_draw) < 3:
	num1 = random.randint(10000, 20000)
	if num1 in lucky_draw:
		pass
	else:
		lucky_draw.append(num1)

print("The winning tickets are as follows:")
counter = 1
for item in lucky_draw:
	print(str(counter) + ". " + str(item))
	counter = counter + 1