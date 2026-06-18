class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        print(s)
        y = "".join(reversed(s))
        print(y)
        return str(y) == s