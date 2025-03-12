print("Hello from lesson 6")

# Task 1

contacts = []
contact1 = ["John", 98453126, "john@gmail.com"]
contact2 = ["Adam", 93029102, "adam@gmail.com"]
contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]
contacts.append(contact1)
contacts.append(contact2)
contacts.append(contact3) 
print(contacts)

for x in contacts:
    print(x)
    for y in x:
        print(y)


# Task 2a

students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]
boys = [
]
girls = [
]
counter1 = 0
counter2 = 0
for student in students:
    name, gender = student
    print(name, ", ", gender)


# Task 2b

    if gender == "F":
        girls.append(name)
        counter1 = counter1 + 1
    elif gender == "M":
        boys.append(name)
        counter2 = counter2 + 1
print(counter1)
print(counter2)



