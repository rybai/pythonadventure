'''
Team Project
Fresh code 12/1/12
'''

household = {}
housesize = int(input('How many members in your household are you budgeting for?'))
while housesize > 0:
    personname = input('Please enter the name of the person you would like to budget for: '.title())
    household[personname] = float(input('What is {0}\'s estimated monthly net salary'.format(personname)))
    housesize = housesize - 1
    
for k, v in household.items():
    print(k, v)
    
print(household)

