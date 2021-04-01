from typing import List
def findingmaxmin(arr:List) ->int:
    return max(arr), min(arr)


def findmax(arr) -> int:
    m =arr[0]
    for x in arr:
        if x > m:
            m =x
    return m
def findmin(arr):
    m=arr[0]
    for x in arr:
        if x< m:
            m =x
    return m
    
    
def main():
    arr =[-1,0,1,4,-4,5,9]
    print(findingmaxmin(arr))
    print("max is ", findmax(arr))
    print("min is ", findmin(arr))
if __name__ =='__main__':
    main()
    