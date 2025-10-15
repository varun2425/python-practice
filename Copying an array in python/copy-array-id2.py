from numpy import *

arr1 = array([2,6,8,1,3])

arr2 = arr1.view()

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))    

# output [2 6 8 1 3]
#        [2 6 8 1 3]
#124308400    #address
#58468776     #address (two different address)