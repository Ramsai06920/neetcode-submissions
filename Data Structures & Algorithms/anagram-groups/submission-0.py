class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = defaultdict(list)
        for word in strs:
            key =tuple(sorted(word))

            dt[key].append(word)

        return list(dt.values())
        