class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        parent_sets = {}
        for i, n in enumerate(strs):
            sorted_string = "".join(sorted(n))
            if sorted_string in parent_sets:
                parent_sets[sorted_string].append(n)
            else:
                parent_sets[sorted_string] = [n]
        return list(parent_sets.values())
