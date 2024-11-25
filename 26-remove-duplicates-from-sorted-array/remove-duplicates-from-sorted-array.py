class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize a pointer for the position of unique elements
        unique_index = 0

        # Iterate through the array
        for i in range(1, len(nums)):
            # Check if the current element is different from the last unique element
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]  # Place the unique element in the next position

        # The number of unique elements is `unique_index + 1`
        return unique_index + 1
