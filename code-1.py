"""
1. Two Sum
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store numbers as keys and their indices as values
        d = {}
        # Iterate over the list of numbers with their indices
        for index_2, num_2 in enumerate(nums):
            # Check if the difference between the target and the current number is in the dictionary
            index_1 = d.get(target - num_2, -1)
            # If the difference is found, return the indices of the two numbers that add up to the target
            if index_1 >= 0:
                return [index_1, index_2]
            # Otherwise, add the current number and its index to the dictionary
            d[num_2] = index_2
        # If no pair is found, return None
        return None

    def twoSum_n2(self, nums: List[int], target: int) -> List[int]:
        # Iterate over the list of numbers
        for i in range(len(nums)):
            # Iterate over the remaining numbers in the list
            for j in range(i + 1, len(nums)):
                # Check if the current pair of numbers adds up to the target
                if nums[i] + nums[j] == target:
                    # If so, return the indices of the two numbers
                    return [i, j]
        # If no pair is found, return None
        return None

# Test cases
solution = Solution()

# Test case 1: Simple example
nums = [2, 7, 11, 15]
target = 9
result1 = solution.twoSum(nums, target)
result2 = solution.twoSum_n2(nums, target)
assert result1 == [0, 1], f"Expected [0, 1] but got {result1}"
assert result2 == [0, 1], f"Expected [0, 1] but got {result2}"

# Test case 2: Edge case - no solution
nums = [3, 3, 5]
target = 10
result1 = solution.twoSum(nums, target)
result2 = solution.twoSum_n2(nums, target)
assert result1 is None, f"Expected None but got {result1}"
assert result2 is None, f"Expected None but got {result2}"

# Test case 3: Edge case - duplicate numbers
nums = [3, 3]
target = 6
result1 = solution.twoSum(nums, target)
result2 = solution.twoSum_n2(nums, target)
assert result1 == [0, 1], f"Expected [0, 1] but got {result1}"
assert result2 == [0, 1], f"Expected [0, 1] but got {result2}"

# Test case 4: Edge case - large numbers
nums = [1000, 1500, 3000, 4000]
target = 5000
result1 = solution.twoSum(nums, target)
result2 = solution.twoSum_n2(nums, target)
assert result1 == [0, 3], f"Expected [0, 3] but got {result1}"
assert result2 == [0, 3], f"Expected [0, 3] but got {result2}"

# Test case 5: Edge case - negative numbers
nums = [-2, -7, 11, 15]
target = -9
result1 = solution.twoSum(nums, target)
result2 = solution.twoSum_n2(nums, target)
assert result1 == [0, 1], f"Expected [0, 1] but got {result1}"
assert result2 == [0, 1], f"Expected [0, 1] but got {result2}"