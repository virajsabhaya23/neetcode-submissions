class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for i, s_char in enumerate(s): 
            ds[s_char] = ds[s_char]+1 if s_char in ds else 1

        for i, t_char in enumerate(t):
            dt[t_char] = dt[t_char]+1 if t_char in dt else 1

        return ds == dt