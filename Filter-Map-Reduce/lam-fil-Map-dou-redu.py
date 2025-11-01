#Here we reduce // instead of having multiple values i want only one value i want to add all these values

from functools import reduce #Here reduce function to module called as function tool

def add_all(a,b): #Any function name and this will take two parameters
    return a+b

nums =[3,2,6,8,4,6,2]

evens = list(filter(lambda n : n%2==0,nums)) 


doubles = list(map(lambda n : n*2,evens)) 

sum = reduce(add_all,doubles)      #if i give 10 values we will add two values at a time that import
#That why we use reduce

print(sum) 


#sum = reduce() <-- here we have to pass two things  1)function and 2)sequnce