# we  can use 'and' and 'or' together.
age1 = int(input("Enter 1st person's age ="))
age2 = int(input("Enter 2nd person's age ="))
age3 = int(input("Enter 3nd person's age ="))

if age1>age2 and age1>age3 and age2>age3:
    print("age1 is oldest and age3 is youngest among all")
elif age2>age3 and age2>age1 and age3>age1 :
    print("age2 is oldest and age1 is youngest among all")
elif age3>age2 and age3>age1 and age1>age2:
    print("age3 is oldest and age2 is youngest among all")
else:
    print("None of the above")