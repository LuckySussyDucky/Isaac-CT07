import random
# Question 1

MonstersFought = 0
HeroHealth = 100
print("Hero starts on his adventure with Health: ", HeroHealth)

if HeroHealth != 0:
    healthLost = random.randint(1, 15)
    HeroHealth = HeroHealth - healthLost
    print("After fighting a monster, his Health is now: ", HeroHealth)
    MonstersFought = MonstersFought + 1
elif HeroHealth > 0:
    healthLost = random.randint(1, 15)
    HeroHealth = HeroHealth - healthLost
    print("After fighting a monster, his Health is now: ", HeroHealth)
    MonstersFought = MonstersFought + 1
else:
    print("The Hero fought ", MonstersFought, "battles, and died.")
