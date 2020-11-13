# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = (name1+name2).lower()
true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") +name.count("o") + name.count("v") + name.count("e")
percentage = true * 10 + love

if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}, you go together like coke and mentor")
elif 40 < percentage < 50:
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}.")