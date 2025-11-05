def div(a,b):
    print(a/b)


def smart_div(func):

    def inner(a,b):
        if a<b:  #logic
            a,b = b,a #swape
        return func(a,b)
    return inner


div1 = smart_div(div)


div1(2,4)

# Amazing part about decorators is you can change the behavior of the existing function at the compile time itself 