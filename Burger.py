print("Hello welcome to Yeriel's Burger shop!!")

#Taking Name 
Name = input("What is your name?\n" )

print("Hello, " + Name + ", Thank you for coming in today")

#menu
#price
BurgerPrice = [9.99, 8.99, 6.99]

#Burger type
strburger = ['Big Burger: ', '\nMedium Burger: ', '\nSmall Burger: ']
SodaPrices = [0.99, 1.99, 2.99]
#Sodas
Soda = ['Small Soda: ', '\nMedium Soda', '\nLarge Soda']

#order 
print("Here is our menu!!\n")
print(strburger[0], BurgerPrice[0])
print(strburger[1], BurgerPrice[1])
print(strburger[2], BurgerPrice[2])

order = input("\nWhat would you like to order?\n")

print ('Ok, I got your buger down')

#soda = input('\nwould you like a soda with your', order, '?\n')

if soda == 'yes':
    print(Soda[0], SodaPrices[0])
    print(Soda[1], SodaPrices[1])
    print(Soda[2], SodaPrices[2])

    SodaOrder = input('Which size would you like?\n')
    SodaOrderconf = input('Are you sure?\n')
    
    if SodaOrderconf == 'yes':
        print("Ok, I'll add that to your order")
 
    


#confirmation
confirm = input("Are you sure you will like a " + order + "?\n")

if confirm == "yes":
    print("Thank, " + Name + " ,your " + order + " will be right up!")
else:
    print('Ok, you order will be cancelled')
