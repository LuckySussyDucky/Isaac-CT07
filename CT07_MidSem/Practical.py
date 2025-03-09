import random
# Question 1

MonstersFought = 0
HeroHealth = 100
print("Hero starts on his adventure with Health: ", HeroHealth)

healthLost = random.randint(1, 15)
HeroHealth = HeroHealth - healthLost
print("After fighting a monster, his Health is now: ", HeroHealth)
