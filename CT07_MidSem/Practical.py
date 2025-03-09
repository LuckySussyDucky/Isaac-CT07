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