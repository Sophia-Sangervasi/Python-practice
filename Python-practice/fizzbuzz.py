def fizzbuzz():
	number = 0 #this is the counter that will start from 0-100
	while(number <= 100):
		if(number%3 == 0 and number%5 == 0):
			print(number , 'Fizzbuzz!')
		
		elif(number %3 == 0 ):
			print(number , 'Fizz \n')

		elif (number%5 == 0):
			print(number , 'Buzz\n')
		
		number+=1
		
			
			

fizzbuzz()