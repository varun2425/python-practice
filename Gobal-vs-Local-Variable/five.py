a = 10


def something():
    
    a = 9

    x = globals() ['a']                      #Here the gobal will give all the glabal variables,BUT here wewant only one variable we will specify

    print("in fun", a)


something()


print("outside", a)
