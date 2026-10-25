class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if counts.get(n, 0) == 0:
                counts.update({n:1})
            else:
                counts[n]+=1
        
        sorted_counts = sorted(counts, key=counts.get, reverse=True)

        return sorted_counts[:k]

        