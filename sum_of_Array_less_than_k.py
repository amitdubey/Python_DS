""" sum of array less than K value given

Returns:
    array nums: Your are given an array of positive integers nums.Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""
from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k<=1: return 0
    prod =1
    ans=left =0
    for right,val in enumerate(nums):
        prod *=val
        while prod >=k:
            prod/=nums[left]
            left+=1
        ans +=right -left +1
    return ans


def main():
    array =[10,5,2,6]
    k =100
    print(numSubarrayProductLessThanK(array, k))

if __name__ == '__main__':
    main()