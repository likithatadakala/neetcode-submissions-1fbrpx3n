class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in range(len(strs)):
            s_s = tuple(sorted(strs[i]))
            if s_s in group:
                group[s_s].append(strs[i])
            else:
                group[s_s] = [strs[i]]
        return list(group.values())
                
                