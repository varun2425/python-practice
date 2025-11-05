def div(a,b):
    print(a/b)


def smart_div(func):

    def inner(a,b):
        if a>b:  #logic
            a,b = b,a #swape


div(2,4)