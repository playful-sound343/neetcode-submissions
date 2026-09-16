class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)

        max_freq=max(count.values())

        max_cunt=sum(1 for cunt in count.values() if cunt==max_freq)

        frame_time=(max_freq-1)*(n+1)+max_cunt

        return max(len(tasks),frame_time)



        
        