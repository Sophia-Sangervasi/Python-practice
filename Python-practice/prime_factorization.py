import math

#This method takes a whole number as an input and returns
#its prime factorization ( a list of whose product is n)
def prime_factorization(number):
  
    # Print the number of two's that divide number 
    while number % 2 == 0: 
        print (2),
        number = number / 2
          
    # number is odd
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(number))+1,2): 
          
        # while i divides n , print i ad divide number 
        while number % i== 0: 
            print (i), 
            number = number / i 
              
    # Condition if number is a prime 
    # number greater than 2 
    if number > 2: 
        print (number)
       
prime_factorization(120)