print("Hello from lesson 8")

# Recap 1

list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]
allNum = [
]
unique = [
]
allNum = list1 + list2 + list3
print(allNum)
for numbers in allNum:
    if numbers not in unique:
        unique.append(numbers)
unique = (sorted(unique))
index = len(unique) // 2
print(unique[:index])
print(unique[index:])


# .isdigit() function is True if all is numbers
# .isalpha() function is True if all is words
# .isalnum() function is True if all is numbers or words
# .isupper() function is True if all is all capital letters
# .islower() function is True if all is all lowercase letters

# is8CharLong = False
# hasupper = False
# haslower = False
# hasnum = False
# onlyalnum = False
# if all correct, password is valid


# Task 1

userInput = input("What would you like your password to be? ")

is8CharLong = False
hasupper = False
haslower = False
hasnum = False
onlyalnum = False

if len(userInput) >= 8:
    is8CharLong = True

hasnum = userInput.isdigit()

