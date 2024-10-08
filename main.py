# Programmers:  Caitlin Burns and Laure Patera
# Course:  CS151, Professor Zee
# Due Date: 10/9/2024
# Lab Assignment: 4
# Problem Statement: this program tells a user how much they owe for their monthly phone bill
# Data In: Package choice and data used
# Data Out:  Total amount due
# Credits: This code is based on the example in the read me file

#this program tells a user how much they owe on their monthly phone bill

#Asks the user what phone package they have of three options, and error checks
package = input('What phone package do you have? ')
package = package.lower()
while package != 'green' and package != 'blue' and package != 'purple':
    print('Invalid package. Please try again.')
    package = input('What phone package do you have? ')
    package = package.lower()

#Finds the price and data used if the user inputs green for their package
if package == 'green':
    price = 49.99
    data = 2
    data_used = int(input('How much data have you used this month?'))
    if data_used > data:
        data_used = data_used - data
        total_price = price + (data_used * 15)
    else:
        total_price = price
    coupon = input('Do you have a coupon? ')
    if coupon == 'yes' and total_price > 75:
        total_price = total_price -20
    elif coupon == 'no':
        total_price = total_price

#Finds the price and data used if the user inputs blue for their package
elif package == 'blue':
    price = 70.00
    data = 4
    data_used = int(input('How much data have you used this month?'))
    if data_used > data:
        data_used = data_used - data
        total_price = price + (data_used * 10)
    else:
        total_price = price

#Finds the price and data used if the user inputs purple for their package
elif package == 'purple':
    total_price = 99.95

#Outputs the final total price to the user based on their package
print(f'You owe ${total_price:.2f}')




