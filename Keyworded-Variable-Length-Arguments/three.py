#Let use for loop

def person(name, **data):

    print(name)

    for i,j in data.items():
        print(i,j)


person('Varun',age=22,city='Guntakal',mob=6303165041)