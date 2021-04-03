"""integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
from typing import List
def maxsubarraysum(arr:List)->None:
    current_subarr=max_subarr=arr[0]
    
    for a in arr[1:]:
        """
        find the positive value only and ignore the negative value -a, 0+(-a)
        """
        current_subarr =max(a, current_subarr+a)
        max_subarr =max(max_subarr,current_subarr)
        
    return max_subarr

def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxsubarraysum(arr))
    
if __name__ == '__main__':
    main()