import random
# Term 1

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



# Term 2

# Question 1

daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 
               13056, 952, 1100, 1025, 8574, 14014, 9987, 
               1238, 1458, 7803, 900, 13674, 14539, 13241, 
               10886, 7541, 8743, 1482, 11523, 977, 12181, 
               8903, 1008, 1530]

# a)

highestSale = 0
for sales in daily_sales:
    if sales > highestSale:
        highestSale = sales
print(daily_sales.index )
print(highestSale, "August has the highest sales of" , highestSale)