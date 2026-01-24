# Check if given
# number is Even or Odd?
# import dictionary

# num = int(input("Enter Number : ", ))
# if num / 2:
# print(" It's Even")
# else:
# print("it's odd")

# Check if number is positive, negative or zero?
#
# num = int(input("Enter a number: "))
#
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# 2 question
# place = (input("Is Sydney the capital of Australia: "))
# if place == "y":
#     print ("Wrong! Canberra is the capital")
# elif place == "n":
#     print ("Correct!")
# else:
#     print ("I do not Understand your answer!")

#Print two number larger of two numbers?

# x = int(input("Enter larger number :"))
# y = int(input("Enter smaller number :"))
#
# if x > y:
#     print("Larger number is :", x)
# elif y > x:
#     print("Smaller number is :", y)
# else:
#     print("Both number are equal")

#Write a program that asks the user for their height in centimeters. If the height is more than 185 centimeters, print “You are very tall.”
#
# height = int(input("Enter your height in centimeters: "))
#
# if height >= 185:
#     print("you are very tall")
# else:
# #     print("you are normal")
#
# places = {
#     "Naimath": "Japan",
#     "Niha" : "Dubai",
#     "Konica" : "Italy"
# }
#
# #names =["Neha", "Naimath", "Konica"]
# Cost ={"Dubai" : 2000, "Italy": 1000, "Japan": "Complimentry free"}
# # name = input ("Enter a name :")
# Place = input("Please enter your place: ")
#
# """Find cost for the place """
# if Place in places.values():
#     print(f"Show the trip price for the place {Place}: ",Cost[Place])





# if name in places:
#     place= places[name]
#     print ("Place:", place)
#     print("Cost:", Cost[place])
# else:
#     print("Sorry, your place does not exist")


# if Cost in names:
#     fav_cost= Cost[name]
#     print(f"{fav_cost} is favorite")
#
#     places = place[fav_cost]
#     print(fav_cost)


# Days = {
#     1 :  "Monday",
#     2 : "Tuesday",
#     3 : "Wednesday",
#     4 : "Thursday",
#     5 : "Friday",
#     6 : "Saturday",
#     7 : "Sunday"
# }
#
# num = int(input("Enter a number (1-7):"))
# if num in Days:
#     print("Day:",Days[num])
# else:
#     print("Invalid number. Please enter number between 1 to 7.")


# x = int(input("Enter a number: "))
# print(x**3)

# Student fee database
# fees = {
#     "Zunu": 45000,
#     "Mahi": 52000,
#     "Ibbu": 48000,
#     "Yusuf": 50000
# }
#
# # Input student name
# name = input("Enter student name: ")
#
# # Find annual fee
# if name in fees:
#     print("Annual fee for", name, "is", fees[name])
# else:
#     print("Student not found")


# Create data set 1: tuple,/list,/dictionary
#
# my_list = ["iphone", "samsung", "mac"]
# my_tuples = ("iphone", "notebook", "ipad")
# my_dic = {
#     "iphone": "white color",
#     "notebook": "red color",
#     "ipad": "green color",
#     "samsung": "yellow color",
#     "mac": "blue color"
# }
#
# item = input("Anything: ")
#
#
# if item in my_list or item in my_tuples:
#     print(" your device in" , my_dic[item])
#
# else:
#     print("Device not found")

Bikes_name =[ "Harleydavidson" , "Enfield", "Kawasaki", "Honda"]
Bike_Description = {
    "Harleydavidson" : "Cruisor",
    "Enfield": "Classic",
    "Kawasaki" : "Sporty",
    "Honda" : "Hness350_Cruiser"
}

bike_price=(100000, 200000, 300000, 400000)

Bike_name=input("Enter bike name:")
if Bike_name in Bike_Description:
    if Bike_name == "Harleydavidson":
        print(f"{Bike_name}Bike Price is: ",bike_price[0])
        print(f"{Bike_name} format is",(Bike_Description[Bike_name]))
    elif Bike_name == "Enfield":
        print(f"{Bike_name}Bike Price is: ",bike_price[1])
        print(f"{Bike_name} format is",(Bike_Description[Bike_name]))
    elif Bike_name == "Kawasaki":
        print(f"{Bike_name}Bike Price is: ",bike_price[2])
        print(f"{Bike_name} format is",(Bike_Description[Bike_name]))
    elif Bike_name == "Honda":
        print(f"{Bike_name}Bike Price is: ",bike_price[3])
        print(f"{Bike_name} format is",(Bike_Description[Bike_name]))
    else:
        print("Bike name not found")
else:
    print("Selection is not in give description- select for below only - Harleydavidson" , "Enfield", "Kawasaki", "Honda ")









