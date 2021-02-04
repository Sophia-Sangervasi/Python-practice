


#This method takes any number and prints out the prime numbers in range
#2<input number 
def primes(num):

   for num in range(2,num):
    if all(num%i!=0 for i in range(2,num)):
       print (num)

       
        
primes(10)
            
