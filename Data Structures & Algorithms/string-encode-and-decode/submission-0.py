class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + f"{len(s)}#{s}"
        return res
    def decode(self, s: str) -> List[str]:
        lis = []
        i = 0
        while i< len(s):
            j=i
            while s[j] != "#":
                j = j+1
            
            n = int(s[i:j])
            lis.append(s[j+1:j+n+1])
            i = j+n+1

        return lis

