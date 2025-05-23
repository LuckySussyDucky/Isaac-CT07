import random
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
onlyalnum = True

if len(userInput) >= 8:
    is8CharLong = True

for i in userInput:
    if i.isupper():
        hasupper = True
    if i.islower():
        haslower = True
    if i.isdigit():
        hasnum = True
    if not i.isalnum():
        onlynum = False

if is8CharLong and hasupper and haslower and hasnum and onlyalnum:
    print("Your password is valid")

# OR

# while True: 
#     pw = input("Enter Password: ")
#     if len(pw) <= 8:
#         print("The password needs to have at least 8 characters.")
#     elif pw.isupper():
#         print("The password needs to have uppercase letters")
#     elif pw.islower():
#         print("The password needs to have lowercase letters")
#     elif pw.isdigit():
#         print("The password need to have a number.")
#     elif pw.isalpha():
#         print("The password need to have a alphabate")
#     elif pw.isalnum():
#         print("The password must have only alphanumerical.")
#     else:
#         print("Password is valid.")


# Task 2

userInput = input("What is your full name? ")
end = ""

for i in range(len(userInput)):
    if i % 2 == 0:
        end = end + userInput[i].lower()
    else:
        end = end + userInput[i].upper()
print("Hello, " + end)
        

# Task 3 

string = "Hi! I am Isaac David Lee Wai Kit!"
list = string.split()
print(list)


# Task 4 

list =  ['Computers',
         'empower',
         'our',
         'modern',
         'world',
         'with',
         'their',
         'digital',
         'brains.']
string = " ".join(list)
print(string)
list = string.split()
print(list)


# Task 5

phrase = "Hello world"
word = phrase.split(" ")
reversedWords = [
]
for letters in word:
    reversedWord = letters[::-1]
    reversedWords.append(reversedWord)
reversedSentence = " ".join(reversedWords)
print(reversedSentence)


# Task 6

phrase = "radar"
word = phrase.split(" ")
reversedWords = [
]
for letters in word:
    reversedWord = letters[::-1]
    reversedWords.append(reversedWord)
reversedSentence = " ".join(reversedWords)
if reversedSentence == phrase:
    print(phrase + " is a palindrome.")
else: 
    print(phrase + " is not a palindrome.")


# Task 7

while True:
    phrase = input("Provide a word: ")
    if phrase != "end":
        word = phrase.split(" ")
        reversedWords = [
]
        for letters in word:
            reversedWord = letters[::-1]
            reversedWords.append(reversedWord)
            reversedSentence = " ".join(reversedWords)
        if reversedSentence == phrase:
            print("It is a palindrome.")
        else: 
            print("It is not a palindrome.")
    else:
        break


# Task 8


phrase = input("Provide a senetence: ")
word = phrase.split(" ")
reversedWords = [
]
reversedPalindrome = [
]
NumOfPalindromes = 0
for letters in word:
    reversedWord = letters[::-1]
    isPalindrome = letters == reversedWord
    if(isPalindrome):
        NumOfPalindromes += 1
        reversedPalindrome.append(reversedWord)
print(NumOfPalindromes)
for word in reversedPalindrome:
    print(word)
