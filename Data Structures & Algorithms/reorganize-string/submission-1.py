class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-cnt, char) for char, cnt in counts.items()]
        heapq.heapify(max_heap)
        
        # Stores tuples of: ((remaining_neg_count, char), ready_time)
        cooldown_q = deque()
        res = []
        time = 0
        
        while max_heap or cooldown_q:
            time += 1
            
            # 1. Unfreeze characters whose cooldown step has expired
            if cooldown_q and cooldown_q[0][1] == time:
                heapq.heappush(max_heap, cooldown_q.popleft()[0])
                
            # 2. Pick the available character with highest remaining frequency
            if max_heap:
                cnt, char = heapq.heappop(max_heap)
                res.append(char)
                
                # 3. If characters remain, send to queue until time + 2
                if cnt + 1 < 0:
                    cooldown_q.append(((cnt + 1, char), time + 2))
            else:
                # Heap is empty while queue still holds characters -> invalid configuration
                return ""
                
        return "".join(res)