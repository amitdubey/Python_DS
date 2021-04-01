list = [[1,4,5,7,8],[4,6,9,10],[12,15,16,17]]

def traversing_list_of_list(list_of_list):
    test=[]
    for i in list:
        #reverse each list of list
        for j in i[::-1]:
            test.append(j)
    return test


    
        
#traversing through tuple of tuple
list_of_tuples = [("Betty", 45), ("John" , 84), ("Malik" , "34"), ("Jose" , 20)]
for index,value in enumerate(list_of_tuples):
    print(index,value)

#traversing through dictionaries

list_of_dictionaries =[{'a': 1}, {'b': 3}, {'c': 5}]
for index in range(len(list_of_dictionaries)):
    for key in list_of_dictionaries[index]:
        print(list_of_dictionaries[index][key])


def main():
    print(traversing_list_of_list(list))
    

if __name__ == '__main__':
    main()