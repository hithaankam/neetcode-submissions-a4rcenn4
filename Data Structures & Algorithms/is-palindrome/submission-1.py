class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.isalnum()]
        print(s)
        return s == s[::-1]
        