"""Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.
Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.

"""
from typing import List
def twoSumLessThanK( nums: List[int], k: int) -> int:
    nums.sort()
    answer = -1
    left =0
    right =len(nums) -1

    while left <right:
        sums =nums[left]+ nums[right]        
        if sums <k:
            answer = max(answer,sums)
            left+=1
        else:
            right -=1
    return answer
    
def main():
    arr = [34,23,1,24,75,33,54,8]
    k =60
    print (twoSumLessThanK(arr,k))
    
    
if __name__ == '__main__':
    main()
    