class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict(Counter(nums))
        sort = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))

        return list(sort.keys())[:k]
        
