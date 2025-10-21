#Scope  // it is possible to create two variable on same code,yes if there have different scope 


a = 10

def something():
    a = 15

    print(a)


print(a)