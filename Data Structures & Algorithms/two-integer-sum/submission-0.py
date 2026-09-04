class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[nums[i]] = i
        return []
