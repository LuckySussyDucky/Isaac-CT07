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
counter = (daily_sales.index(max(daily_sales))) + 1
print(counter, "August has the highest sales of $" + str(highestSale))

# b)

lowestSale = highestSale
for sales in daily_sales:
    if sales < lowestSale:
        lowestSale = sales
counter = (daily_sales.index(min(daily_sales))) + 1
print(counter, "August has the lowest sales of $" + str(lowestSale))

# c)

print("Average daily sales for August is $" + str(round(sum(daily_sales) / len(daily_sales), 2)))


# Question 2

list = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
for i in list:
    isEven(i)
    if True:
        print("It is an even number.")
    else: 
         print("It is an odd number.")