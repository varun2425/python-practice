#Here we will reduce the steps as compare to previous one(lambda-Mpp.py)


nums =[3,2,6,8,4,6,2,9,10,12,98]

evens = list(filter(lambda n : n%2==0,nums)) 


doubles = list(map(lambda n : n+2,evens))

print(evens)
