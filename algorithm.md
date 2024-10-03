# Algorithm Document

1. Ask the user to input what package they have 
3. while package is not equal to green, blue or purple
   1. Output 'That was an invalid package. Try again.'
   2. Ask the user what package they have
   3. convert input to lowercase
4. if package = Green
   1. Set variable price to 49.99
   2. Set GB_data equal to 2
   2. ask user how much data they used in GBs as a float
   4. if GB_data > 2
      1. price = 49.99 + (GB_data * 15)
   6. ask if customer has a coupon
   7. if yes and price > 75
      1. subtract 20 from price
5. if package = Blue
   2. Set variable price to 70
   3. Set GB_data to 4
   2. ask user how much data they used in GBs as a float
   4. if GB_data > 4
      1. price = 70 + (GB_data * 10)
6. if package = Purple
   1. set the variable price equal to 99.95
   2. ask user how much data they used in GBs as a float
7. output to user price and GB_data



