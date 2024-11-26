class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Use a set to find missing numbers efficiently
        n = len(nums)
        full_set = set(range(1, n + 1))  # Expected numbers from 1 to n
        nums_set = set(nums)            # Unique numbers in the array
        
        # Find the difference between the sets
        missing = list(full_set - nums_set)
        return missing
