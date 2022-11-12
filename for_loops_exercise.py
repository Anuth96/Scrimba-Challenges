names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
#First lets combine these two lists
names.extend(names1)
#Then ask for user input if they would like to add any new friends
user_input = input('Would you like to add any new Friends to your invitation list? (Y/N)').strip()
while user_input.lower() == 'y':
    names.append(input('Please enter your Friends full name: ').strip())
    user_input = input('Would you like to add another? (Y/N)').strip()
else:
    print('\nOkay here are your invitations......')
#Now lets create a for loop for each invitation
for element in names:
    print(f'{element.title()}! You are invited to the party on Saturday.')
