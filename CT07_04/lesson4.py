print("Hello from lesson 4")

# Task 1a

planet = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
# print(planet[0])
# print(planet[1])
# print(planet[2])
# print(planet[3])
# print(planet[4])
# print(planet[5])
# print(planet[6])
# print(planet[7])


# Task 1b

planet[3] = "Mars -> defeated"
for i in range(len(planet)):
    print(planet[i])


# Task 1c

planet.insert(8, "Pluto -> new planet discovered")

planet[3] = "Mars -> defeated"
for i in range(len(planet)):
    print(planet[i])

planet.insert(3, "Lalaland -> new planet discovered")
for i in range(len(planet)):
    print(planet[i])


# Task 1d

planet.pop(5)
for i in range(len(planet)):
    print(planet[i])


# Task 2

planet = [
    "Mercury",
    "Venus",
    "Earth",
    "Lalaland",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
for i in range(len(planet)):
    if planet[i] == "Earth":
        print("Earth: This is my home!")
    elif planet[i] == "Lalaland":
        print("Lalaland: This is what I created!")
    elif planet[i] == "Mars":
        print("Mars: I conquerd this!")


# Task 3

countriesIwouldLiketoVisit = []
country = ""
while country != "end":
    country = input("What country would you like to visit? ")
    countriesIwouldLiketoVisit.append(country)
countriesIwouldLiketoVisit.pop(len(countriesIwouldLiketoVisit)- 1)
for i in range(len(countriesIwouldLiketoVisit)):
    print("I would like to visit", countriesIwouldLiketoVisit[i])


# Task 4a

menu = []
food = ""
while food != "end":
    food = input("What food should you add to the menu? ")
    menu.append(food)
menu.pop(len(menu)- 1)
for i in range(len(menu)):
    print("- ", menu[i])


# Task 4b

FoodToEat = input("What would you like to eat? ")
food = ""
while food in menu:
    if food == FoodToEat:
        print("Yes, we have that. Anything else?")
        break
    else:
        print("Sorry (but not sorry) we don't have that")
