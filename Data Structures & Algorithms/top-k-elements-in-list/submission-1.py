import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #   top k frequent means you can create a heap of lenght k
    #  use count collecton to create a hashmap of frequencies it will be faster

        freq_map = Counter(nums)

        heap = []

        for num, frequency in freq_map.items():
            heapq.heappush(heap, (frequency, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for frequency, num in heap]
        