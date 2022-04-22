import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Gets the number of names in the list
number_of_names = len(names)

#finds a random number, searching 0 through (denoted by the -1) the number of names
random_number = random.randint(0, number_of_names -1)
#searches the list for the [object that matches the random_number
payer = names[random_number] 
print(payer + "Is paying today.")

