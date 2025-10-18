#Variable Length Arugument

def sum(*b):
    
    c = 0

    for i in b:            #Here 'b' is a tuple
        c = c + i

    print(c)

sum(5,6,34,78)