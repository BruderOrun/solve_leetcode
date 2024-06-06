from typing import List


class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """

    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     return next((i, j) for i, x in enumerate(nums) for j, y in enumerate(nums[i+1:], i+1) if x + y == target)
    # @classmethod
    # def twosum(cls, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] == target - nums[i]:
    #                 print(i, j)
    #                 return [i, j]
    @classmethod
    def twoSum(cls, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.twoSum(nums, target))
