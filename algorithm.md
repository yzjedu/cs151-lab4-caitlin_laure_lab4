# Algorithm Document

1. Ask the user what package they have
2. convert input to lowercase
3. while package is not equal to green, blue, purple
   1. Output 'That was an invalid package. Try again.'
   2. Ask the user what package they have
   3. convert input to lowercase
4. if package = Green
   1. monthly cost is $49.99 and data is 2GB
   2. ask user how much data they used in GB they used
   3. convert GB to float
   4. if GB>2
      1. charge $15 per extra GB
   5. otherwise 
      1. leave original price of $49.99
   6. ask if customer has a coupon
   7. if yes and bill > $75
      1. subtract $20 from total bill
5. if package = Blue
   1. monthly cost is $70 and data is 4GB
   2. ask user how much data in GB they used
   3. convert GB to float
   4. if GB > 4
      1. charge$10 per extra GB
   5. otherwise
      1. leave original price of $70
6. if package = Purple
   1. monthly cost is $99.95 and data is unlimited
7. output total price and total data used



