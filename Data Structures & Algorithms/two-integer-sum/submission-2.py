class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i , num in enumerate(nums):
            comp = target - num

            if comp in diff:
                return [diff[comp], i]

            diff[num]=i
        