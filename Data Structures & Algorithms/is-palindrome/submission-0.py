class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        print(s)
        y = "".join(c for c in reversed(s) if c.isalnum())
        print(y)
        return str(y) == s