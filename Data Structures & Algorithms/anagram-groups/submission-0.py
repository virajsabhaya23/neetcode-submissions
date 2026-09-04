class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapper = {}
        for word in strs:
            k = tuple(sorted(word))
            mapper.setdefault(k, []).append(word)

        return list(mapper.values())