#Practice Project - Household Financial Freedom
#Developer - JeffreyAlan
#Last Update - 11/18/2012

print('Welcome to Financial Freedom','\n')
#Enter Gross Annual Income
agi=round(float(input('Please enter your annual gross income: ')),2)
print('\n','You entered $',agi,' for your annual gross income! Woot!',sep='')
#Enter Federal Tax Rate
taxrf=round(float(input('\nPlease enter your federal income tax rate %: ')),2)
print('\nYou entered a tax rate of ',taxrf,'% ...ouch!',sep='')
taxrf=taxrf/100
#Enter State Tax Rate
taxrs=round(float(input('\nPlease enter your state income tax rate %: ')),2)
print('\nYou entered a tax rate of ',taxrs,'% ...yowza!',sep='')
taxrs=taxrs/100
#Calc Federal Liability
taxf=round(float(agi*taxrf),2)
#Calculate State Liability
taxs=round(float(agi*taxrs),2)
#Calculate Annual Net Income
ani=round(float(agi-taxf-taxs),2)
#Print Tax Liability Breakdown
print("\nOkay, let's take a look at how dreadful taxes are:")
print('\nYour federal tax liability is $',taxf,sep='')
print('Your state tax liability is $',taxs,sep='')
print('Your net annual income is $',ani,sep='')
#Calculate Monthly Net Income
netinc=round(float(ani/12),2)
print('Your net monthly income is $',netinc,sep='')
#Enter $ Spent on Housing
rent=round(float(input("\nHow much do you spend on rent every month? : ")),)
elect=round(float(input("\nHow much do you spend on electricity every month? : ")),)
gas=round(float(input("\nHow much do you spend on gas every month? : ")),)
cable=round(float(input("\nHow much do you spend on cable+internet utilities every month? : ")),)
otherutil=round(float(input("\nHow much do you spend on other utilities every month? : ")),)
cell=round(float(input("\nHow much do you spend on your cell phone every month? : ")),)
#Enter $ Spent on Debt
#Enter $ Spent on Fixed
#Enter $ Spent on Savings
save=round(float(input("\nHow much do you save every month? : ")),)
#Enter $ Spent on Discretionary
#Calc % of Housing
housing=rent+elect+gas+cable+otherutil+cell
print('\nYou spend $',housing,' on housing each month.',sep='')
housingperc=round(float(housing/netinc),2)
print('\nHousing costs represent',housingperc,'of your net income each month.')
#Calc % of Debt
#Calc % of Fixed
#Calc % of Savings
#Calc % of Disc.