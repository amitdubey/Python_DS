class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            remaining =target-value
            if remaining in seen:
                return [seen[remaining],index]
            seen[value] =index
        return []


def main():
    nums =[1,2,4,5,9,3,6]
    target =9
    s =Solution()
    return print(s.twoSum(nums,target))


if __name__ == '__name__':
    main()
    