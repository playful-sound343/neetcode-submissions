class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted([(enqueue, proc, i) for i, (enqueue, proc) in enumerate(tasks)])
        
        res = []
        min_heap = []  # Stores (processingTime, originalIndex)
        curr_time = 0
        i = 0
        n = len(tasks)
        
        while i < n or min_heap:
            # Fast-forward CPU clock if idle and no tasks are waiting in the heap
            if not min_heap and curr_time < indexed_tasks[i][0]:
                curr_time = indexed_tasks[i][0]
            
            # Enqueue all tasks that have arrived by curr_time
            while i < n and indexed_tasks[i][0] <= curr_time:
                heapq.heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1
            
            # Pop the shortest available job (heap breaks ties with smallest index)
            proc_time, index = heapq.heappop(min_heap)
            curr_time += proc_time
            res.append(index)
            
        return res


        