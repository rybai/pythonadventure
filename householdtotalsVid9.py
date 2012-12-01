# Learning project to establish a household income

# Begin with gathering names and income levels
person1 = input('Please enter the first household members full name: ').title()
person2 = input('Please enter the second household members full name: ').title()
income1 = int(input("Please enter {0}'s gross yearly income: ".format(person1)))
income2 = int(input("Please enter {0}'s gross yearly income: ".format(person2)))
houseinc = income1 + income2 #sum of previous inputs to establish a household income

# Run some basic math and display each person's contribution to the household income
print('You have a combined household income of', '${:,}'.format(income1 + income2))
print("\t{0}'s income of ${1} accounts for {2}% of the total household income.".format(person1, '{:,}'.format(income1), round((income1 / houseinc)*100)))
print("\t{0}'s income of ${1} accounts for {2}% of the total household income.".format(person2, '{:,}'.format(income2), round((income2 / houseinc)*100)))

# Part two, starting a fixed budget
print('\nNow lets gather some information to start a budget...\n')
avgtax = float(input("Please enter your household's estimated effective tax rate: %")) #float() predefines the input to save us from doing it later
netmonth = round(((1-(avgtax/100)) * houseinc) / 12)
print("Accounting for your household's tax rate, your estimated monthly net income is ${0}".format('{:,}'.format(netmonth)))

# Hard coded dictionary - for i statement runs through each stored key in the budgets dictionary
budgets = {'Entertainment':.075, 'Housing':.27, 'Utilities':.11}
for i, v in budgets.items():
    print('We recommend around {0}% of your monthly income go torward {1}. Using this figure, your estimated monthly budget for {2} is ${3}.'.format(v * 100, i.lower(), i.lower(), '{:,}'.format(round(netmonth * v))))

# Test for adding value to our dictionary, reprint entire budget with for statement
budgyn = input("Would you like to add a custom item to your budget? Y/N").lower()
while budgyn[0] == 'y': #the [0] tells the while statement to just check the first charachter in the string, so it'll catch yes, y, yep, etc.
    manbudget = input('What additional item would you like to budget for?')
    budgets[manbudget] = float(input('Ok, now what percentage of your monthly income do you want to allocate towards {0}?'.format(manbudget))) / 100
    budgyn = input('\nOK, so we have added a budget for {0} with a monthly allowance of {1}%. Would you like to add another budget? Y/N\n'.format(manbudget.lower(), budgets[manbudget] * 100)).lower()
    if budgyn[0] == 'n':
        print('\nLets review our new budget with the items you have added:')
        for i in budgets:
            print('\t{0}: ${1}'.format(i.title(), '{:,}'.format(round(netmonth * budgets[i]))))

mainmenu = int(input('Please select from the following options: \
\t1: Display budget in a yearly format \
\t2: Establish a savings budgets \
\t3: Simple Roth IRA calculation \
\t4: Exit program'))

if mainmenu == 1:
    for i in budgets:
        print('\t{0}: ${1}'.format(i.title(), '{:,}'.format(round((netmonth * 12) * budgets[i]))))
    print('Total: {0}'.format(sum((budgets.values() * netmonth) * 12)))
elif mainmenu == 2:
    totalbudgets = 0
    for i in budgets:
        budgets += i
    print('With the items you have budgeted so far, you have a total monthly expense of {0}. This leave you with {1} left over every month.'.format(totalbudgets, netmonth - totalbudgets))
    budgets[savings] = float(input('How much money would you like to save each month?: $'))
    print('\nLets review our new budget now that we\'re saving:')
    for i in budgets:
        print('\t{0}: ${1}'.format(i.title(), '{:,}'.format(round(netmonth * budgets[i]))))
    print('Total: {0}'.format(totalbudgets + budgets[savings]))
elif mainmenu == 3:
    if houseinc < 173000:
        print('With a combined income of ${0} you\'re below the 2013 household contribution limit of $173,000. Lets do a quick exercise to show the power of compound interest and tax free earnings!'.format('{:,}'.format(houseinc)))
        age = int(input('How old are you?'))
        toretire = 65 - age
        rothcont = float(input('You\'ve got {0} years til you retire, we can work with that! As of 2013, the contribution limit for a dual income household is $11,000. How much would you like to contribute?: $'.format(toretire)))
        rothreturn = (rothcont * toretire) * (1 + (.1059 / 12) ** (12 * toretire))
        print('Now we can see the magic! If you start this year and contribute ${0} every year for the next {1} years, you\'ll have ${2} in principal deposits. However, due to the magic of compound interest, if you invested in a broad market ETF with an average annualized 10.59% return you\'ll have ${3} waiting for you when you retire! That is a tax free ${4} in your pocket!'.format('{:,}'.format(int(rothcont)), toretire, '{:,}'.format(int(rothcont * toretire)), int(rothreturn), '{:,}'.format(rothreturn - (rothcont * toretire))))
    else:
        print('First world problem - you make too much money to contribue to a Roth IRA!')
elif mainmenu == 4:
    sys.exit
else:
    print('You entered an invalid option!')

