#We have inbuild function called as fliter in python


def is_even(n):
    return n%2==0

nums =[3,2,6,8,4,6,2,9]

evens = list(filter(is_even,nums)) #Filter will take the list from you ,it will Filter this list ,it will give you the values (IF you say i want even number it give the even number based on you list)// Filter will give you something i want a list out of it and that should work

print(evens)

#Filter will take two arguments 
#1.Function (Which you will mention the logic)
#2.List/sequence