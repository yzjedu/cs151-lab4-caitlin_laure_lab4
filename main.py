# Programmers:  Caitlin Burns and Laure Patera
# Course:  CS151, Professor Zee
# Due Date: 10/9/2024
# Lab Assignment: 4
# Problem Statement: this program tells a user how much they owe for their monthly phone bill
# Data In: Package choice and data used
# Data Out:  Total amount due
# Credits: This code is based on the example in the read me file

#this program tells a user how much they owe on their monthly phone bill

package = input('What phone package do you have? ')
package = package.lower()
while package != 'green' and package != 'blue' and package != 'purple':
    print('Invalid package. Please try again.')
    package = input('What phone package do you have? ')
    package = package.lower()

#works if input is green
if package == 'green':
    price = 49.99
    data = 2
    data_used = input('How much data have you used this month?')
    data_used = int(data_used)
    if data_used > data:
        additional_data = data_used - data
        total_price = price + (additional_data * 15)
    else:
        total_price = price
    coupon = input('Do you have a coupon? ')
    if coupon == 'yes' and total_price > 75:
        total_price = total_price -20
    elif coupon == 'no':
        total_price = total_price
#works if input is blue
elif package == 'blue':
    price = 70.00
    data = 4
    data_used = input('How much data have you used this month?')
    data_used = int(data_used)
    if data_used > data:
        additional_data = data_used - data
        total_price = price + (additional_data * 10)
    else:
        total_price = price
#works if input is purple
elif package == 'purple':
    price = 99.95
    total_price = price

print(f'You owe ${total_price:.2f}')




