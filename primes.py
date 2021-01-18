
def primes(num):
    counter = 1
    results=[] #the array to hold all the primes of 1 - num
    while(counter <= num):
        if(counter % 1 == 0 and counter % num == 0):
            results.append(counter)

        counter+=1
    return results


            
