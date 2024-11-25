class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Clean the string - remove non-alphanumeric characters and convert to lowercase
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Step 2: Use two pointers to check if the string is a palindrome
        left, right = 0, len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        
        return True


        