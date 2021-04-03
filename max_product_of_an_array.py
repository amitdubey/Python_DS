
"""
max product of array 
"""
from typing import List
def maxproductarr(arr:List)->None:
    if len(arr)==0:
        return 0 
    maxarrsofar =arr[0]
    minarrsofar=arr[0]
    result =maxarrsofar
    
    for i in range(1, len(arr)):
        curr=arr[i]
        tempmax= max(curr,maxarrsofar*curr,minarrsofar*curr)
        minarrsofar =min(curr,maxarrsofar*curr,minarrsofar*curr)
        
        maxarrsofar =tempmax
        result =max(maxarrsofar,result)
    return result

def main():
    arr =[6,-2,-4,0,1,3,1,7]
    print(maxproductarr(arr))

if __name__ == '__main__':
    main()
