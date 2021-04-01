from typing import List
array = [1,2,3,3,3,4,5,5,4,6,7,8]
arr =["b", "b", "c", "d","c",1,1,1,3,4,4,4,"c"]

dict ={}
def count_frequency(arr) ->dict:
    dict={}
    for i in arr:
        if i in dict:
            dict[i] +=1
        else:
            dict[i]=1
    return dict

def main():
    print(count_frequency(arr))

if __name__ == '__main__':
    main()
    