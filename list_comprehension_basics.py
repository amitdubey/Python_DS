
#flattening the list 
vec = [[1,2,3], [4,5,6], [7,8,9]]

print([num for elem in vec for num in elem])

lst=[1,2,3,4,5,6]
#list in place square
print([i*i for i in lst])

#increment of list by n number

print([(i+1) for i in lst])