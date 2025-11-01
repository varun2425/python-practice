#Now we will double the value ,so whatever even numbers you got i want to double it
#2 should be 2*2=4 , like this

def update(n):
    return n+2

nums =[3,2,6,8,4,6,2,9,10,12,98]

evens = list(filter(lambda n : n%2==0,nums)) 

#Map i use here

doubles = list(map(update,evens))

print(evens)
