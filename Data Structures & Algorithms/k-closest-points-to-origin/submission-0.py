class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_dist=[(x**2+y**2,x,y) for x,y in points]

        heapq.heapify(min_dist)

        result=[]

        for _ in range(k):
            dist,x,y=heapq.heappop(min_dist)
            result.append([x,y])

        return result


        