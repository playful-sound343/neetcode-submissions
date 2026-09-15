class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n_e=[-n for n in nums]

        heapq.heapify(n_e)

        for _ in range(k-1):
            n_e1=heapq.heappop(n_e)

        return -heapq.heappop(n_e)



        