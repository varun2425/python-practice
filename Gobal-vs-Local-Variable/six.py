#let print id's 


a = 10
print(id(a))

def something():
    
    a = 9

    x = globals() ['a']   
    print(id(x))
    print("in fun", a)


something()


print("outside", a)
