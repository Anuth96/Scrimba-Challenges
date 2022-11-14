#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'Freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

cart = {}
purse={'gold': 1000}
#Freelancers store
print(f'Welcome to the \'{freelancers["name"]}\'\n')
freelancers.pop('name')
for items, price in freelancers.items():
    print(f'{items}: {price} gold')

user_input = input('Which Ally would you like to purchase?\nOr type \'exit\' to leave the store!').strip()

while True:
    if user_input.lower() == 'exit':
        print('Thanks for stopping by!\n')
        break
    elif user_input in freelancers:
        print(f'{user_input.title()} has been purchased as an Ally!\n')
        price = freelancers.pop(user_input)
        cart.update({user_input: price})
        break
    else:
        print('That Ally doesn\'t exist in the shop!!')
        user_input = input('Try again!! Which Ally you like to purchase?')

#Antique store
print(f'Welcome to the \'{antiques["name"]}\'\n')
antiques.pop('name')
for items, price in antiques.items():
    print(f'{items}: {price} gold')

user_input = input('What Item you like to purchase?\nOr type \'exit\' to leave the store!').strip()

while True:
    if user_input.lower() == 'exit':
        print('Thanks for stopping by!\n')
        break
    elif user_input in antiques:
        print(f'{user_input.title()} has been purchased!\n')
        price = antiques.pop(user_input)
        cart.update({user_input: price})
        break
    else:
        print('That Item doesn\'t exist')
        user_input = input('Try again!! What Item would you like to purchase?')

#Pet shop
print(f'Welcome to the \'{pet_shop["name"]}\'\n')
pet_shop.pop('name')
for items, price in pet_shop.items():
    print(f'{items}: {price} gold')

user_input = input('Which Pet you like to purchase?\nOr type \'exit\' to leave the store!').strip()

while True:
    if user_input.lower() == 'exit':
        print('Thanks for stopping by!\n')
        break
    elif user_input in pet_shop:
        print(f'{user_input.title()} has been purchased as a Pet!\n')
        price = pet_shop.pop(user_input)
        cart.update({user_input: price})
        break
    else:
        print('That Pet doesn\'t exist')
        user_input = input('Try again!! Which Pet would you like to purchase?')

#total after purchases using purse
