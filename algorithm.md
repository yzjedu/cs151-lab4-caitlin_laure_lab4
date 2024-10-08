# Algorithm Document

1. Ask the user to input what package they have 
2. convert answer to lowercase
3. while package is not equal to green, blue and purple
   1. Output 'That was an invalid package. Try again.'
   2. Ask the user what package they have
   3. convert input to lowercase
4. if package = Green
   1. Set variable price to 49.99
   2. Set data equal to 2
   2. ask user how much data they used this month, creating the variable data_used
   4. if data_used > data
      1. subtract data from data_used
      2. create the variable total_price and do the equation total_price = price + (data_used * 15)
   6. Otherwise 
      1. the variable total_price is set equal to the value of the variable price
   7. ask if customer has a coupon
   8. convert the answer to lower case
   7. if the answer is yes and price > 75
      1. subtract 20 from price
5. Otherwise if package = Blue
   2. Set variable price to 70
   3. Set data to 4
   2. ask user how much data they used this month, creating the variable data_used
   4. if data_used > data
      1. subtract data from data_used
      2. create the variable total_price and do the equation total_price = price + (data_used * 15)
   6. Otherwise 
      1. the variable total_price is set equal to the value of the variable price
6. Otherwise if package = Purple
   1. set the variable price equal to 99.95
7. output to user price with two decimal places


