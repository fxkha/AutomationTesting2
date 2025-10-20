#the first program
print("Hello World")

#program to print a shape(triangle)
print("     /|")
print("    / |")
print("   /  |")
print("  /___|")

#variable - container to store data.
print("There once was a man named John")
print("He was 34 years old.")
print("He really liked the name John")
print("But didn't liked to be 34")

#adding variable to the above program
character_name = "King"
character_age = "35"
print("There once was a man named " +  character_name + ".")
print("He was " + character_age + " years old.")
print("He really liked the name " + character_name + ".")
print("But didn't liked to be 34")

#working with string
print("Giraffe\nAcademy") #\n means to add a new line
print("Giraffe\"Academy") #\ to add quotation which also means escape character
phrase = "Giraffe Academy" # storing Giraffe Academy in variable
print(phrase)
print(phrase +  " is cool") #concatination which means adding string on a string

#using functions in strings
print(phrase.lower()) #to convert the string in lower case
print(phrase.upper()) #to convert the string in upper case
print(phrase.isupper()) #to check if the string is in upper case
print(phrase.islower()) #to check if the string is in lower case
print(phrase.upper().isupper()) #to convert the string in upper and then check the string its upper or not
print(len(phrase)) #to check the length of the string
print(phrase[0]) #to print a specific string as in python string starts with 0
print(phrase.index("G")) # to print the index of a string
print(phrase.replace("Giraffe", "Lion")) # to replace the string we use .replace
#working with numbers
print(2.67686868)
print(2-1)
print(10*(75765765675+768687)) #multiple
print(10%(75765765675+768687))

my_num = 5 #storing number as a variable
print(my_num)
print(str(my_num) + " is my favourite") #converting number to string
my_num = -5
print(my_num) #to print the absolute value
print(pow(4, 2)) #to calculate the power of the number
print(max(4, 6)) #to print the maximum number
print(min(4, 6)) #to print the minimum number
print(round(4.6)) #to print the round number of the value

from math import * #to import the maths functions

print(floor(3.7)) #to print the floor value
print(ceil(3.7)) #to print the roundup highest value
print(sqrt(225)) #to print the square root of the number

#Getting inputs from user
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + "! You are " + age)

#building a basic calculator
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)
#print(result)

#mad libs game
#color = input("Enter a color: ")
#plural = input("Enter a plural: ")
#celebrity = input("Enter a celebrity: ")
#print("Roses are " + color)
#print(plural + " are blue")
#print("I love " + celebrity)

#list
friends = ["John", "Michael", "Jim", "Oscar", "Jenny"]
print(friends)
print(friends[-2]) #indexing to print a specific value from the list
print(friends[1:3])  #indexing to access two or more values in list
friends[1] = "Zak" #to update an element in list
print(friends)

#list functions
friends = ["John", "Michael", "Jim", "Oscar", "Jenny"]
lucky_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
friends.extend(lucky_numbers) #to join one or more list
print(friends)
friends.append("Kiran") #to add an element at the end of the list
print(friends)
friends.insert(1, "Kelly") #to add an element in a specidic index
print(friends)
friends.remove("Kiran")  #to remove an element
print(friends)
#friends.clear() #to reset a list
#print(friends)
friends.pop() #to remove the last element in the list
print(friends)
print(friends.index("Kelly")) #to know the index of an element and also check if the element is present in list
print(friends.count("Kelly")) #to know the count of an element in a list
friends = ["John", "Michael", "Jim", "Oscar", "Jenny"]
lucky_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
friends.sort() #to sort a list in ascending order
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

#tuples
#tuple is a type of data structure like a container where we can store various values
#its like a list

coordinates = (4, 5) #you can't change the values of tuples in further program-its like whats you write what you get
#coordinates[1] = 10
print(coordinates[0])

#functions
def say_hi(name, age):
    print("hi " + name + "you are " + str(age))
    return "hi " + name + "you are " + str(age)



print("Top")
say_hi("Mike", 35)
say_hi("Steve", 42)

#return
def cube(num):
    return num ** 3
result = cube(5)
print(result)

#ifstatement
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but tall")
else:
    print("You neither are male nor tall")

#if statement and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(100, 20, 30))

#building a better calculator
num1 = float(input("Enter a number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter a number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Invalid operator")

#list
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "october"
}

print(monthConversion.get(("Luv", "Not a valid key")))

#list
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "october"
}

print(monthConversion.get(("Luv", "Not a valid key")))

#whileloop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with the loop")

#building guessing game
secret_word = 'Giraffe'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, you guessed too high")
else:
    print("You win")
