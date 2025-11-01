#Atone point it will take two 

from functools import reduce 


nums =[3,2,6,8,4,6,2]

evens = list(filter(lambda n : n%2==0,nums)) 


doubles = list(map(lambda n : n*2,evens)) 

print(doubles) #Here it will give the list of the number and double the value

sum = reduce(lambda a,b: a+b,doubles)     #we use lambda instead of add_all


print(sum) 
