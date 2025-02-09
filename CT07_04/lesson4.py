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
    planet[i]
    if planet == "Earth":
        print("Earth: This is my home!")
    elif planet == "Lalaland":
        print("Lalaland: This is what")