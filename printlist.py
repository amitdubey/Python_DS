
# _lst =[0,1,2,3,4,5,6,7,8,9]

# _lst[:] =[x+1 for x in _lst]
# print(_lst)
    
    
list = [1,2,3,4,5]

# for index in range(len(list)):
#       list[index] = list[index] +1

# print(list)

# list =[x.__add__(1) for x in list]

# print(list)

def incr(lst, i):
    return [x+i for x in lst]

print(incr(list,1))
    