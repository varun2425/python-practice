
     #WE dont use this one

a = 10

def something():
    global a   # hey python my intention here is use to gobal variable not local variable // WE DONT USE IT IS NOT A GOOD IDEA
    a=15       #if you want to gobal variable you have to use keyword for global ,so you can access it
    print("in fun",a)

    
something()


print("outside",a)