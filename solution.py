import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, i)
            else:
                heapq.heappush(heap, i)

        return heapq.nsmallest(1, heap)[0]