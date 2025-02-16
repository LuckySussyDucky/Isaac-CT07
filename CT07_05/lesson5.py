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
counter = heightlist.index(minimum)
name = namelist[counter]
print(minimum)
print(counter)
print(name)


# Task 5

pokemon = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff",
    "Meowth", "Psyduck", "Eevee", "Snorlax", "Mewtwo",
    "Lapras", "Gengar", "Dragonite", "Machamp", "Arcanine", 
    "Alakazam", "Gyarados", "Vaporeon", "Scyther", "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]
pokemon1 = random.choice(pokemon)
counter1 = pokemon.index(pokemon1)
power1 = powers[counter1]
pokemon2 = 0 
while pokemon1 == pokemon2:
    pokemon2 = random.choice(pokemon)
    counter2 = pokemon.index(pokemon2)
    power2 = powers[counter2]

print(pokemon1, "power", power1, "Versus", pokemon2, "power", power2)

if power1 > power2:
    print(pokemon1, "is the winner!")
elif power1 == power2:
    print("Tie!")
else:
    print(pokemon2, "is the winner!")