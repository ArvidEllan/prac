import coffee_shop

print("welcome to", coffee_shop.shop_name)
print("available sizes:",coffee_shop.coffee_sizes)
print("available roasts:",coffee_shop.coffee_roasts)

#get some inputs from the user
order_size = input("what size coffee do you want")
order_roast = input("what roast do you want")

#Send the order to the coffee shop module
shop_says = coffee_shop.order_coffee(order_size,order_roast)
#print whatever it says back
print(shop_says)

#see if user wants to add milk
add_milk_reponse = input("Do you want to add milk (y/n)?")
#convert to lowecase and check for yes
if "y" in add_milk_reponse.lower():
    milk_fat = input("what percentage milk do you want added ?")
    shop_says = coffee_shop.add_milk_please(milk_fat)
    
    print(shop_says)