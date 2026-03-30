class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanText = "".join(char for char in s if char.isalnum())
        cleanText = cleanText.lower()

        left = 0 
        right = len(cleanText) - 1
        while left < right:
            if cleanText[left] != cleanText[right]:
                return False
            else:
                left = left + 1
                right = right - 1

        return True
