"""array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
"""
from typing import List

def subarrsumk(arr:List[int],k: int)->int:
    dict ={0:1}
    count = 0
    s =0
    
    for i in arr:
        s+=i
        if (s-k) in dict:
            count+=dict[s-k]
        if s in dict:
            dict[s]+=1
        else:
            dict[s]=1
    return count

def main():
    arr =[1,1,1]
    k =2
    print(subarrsumk(arr,k))

if __name__ == '__main__':
    main()