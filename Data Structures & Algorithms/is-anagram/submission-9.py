class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}
        for i in s:
            if i in count_map:
                count_map[i] = count_map[i]+1
            else:
                count_map[i] = 1
        for i in t:
            if i in count_map:
                count_map[i] = count_map[i]-1
            else:
                return False
        for k in count_map.values():
            if k != 0:
                return False
        return True
