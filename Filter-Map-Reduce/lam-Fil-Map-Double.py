

nums =[3,2,6,8,4,6,2,9,10,12,98]

evens = list(filter(lambda n : n%2==0,nums)) 


doubles = list(map(lambda n : n*2,evens)) #here we will change n+2 into = n*2 //beacuse you want to double



print(doubles) #Here dwe use doubles you will get the same stuff but you are saying plus 2