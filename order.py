#show tittle
print ("WELLCOME TO OURS STORE")
print ("_____PI77A CRUSH______")

print("Input Your Name : ")
name = input()  # get user name
print("Input Your Table : ")
table = input() #get user table

total_hrga = 35000

#showing topping menu
print("Our Topping Menu, Pelase choose one ")
print("frankfuter bbq, meat monsta, super supreme, chicken lovers, cheese lovers, and american fav")
topping = input("Enter our fav toppings : ")
if topping == "frankfurter bbq" or topping == "meat monsta" or topping == "super supreme" or topping == "chicken lovers" or topping == "cheese lovers" or topping == "american fav":
    total_hrga = 50000 #get topping price
else:
    total_hrga = 0
    print("Sorry, your fav topping was sold out/nothing")

#contoh
