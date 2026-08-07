class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices of days

        for i, temp in enumerate(temperatures):
        # While the current temp is warmer than the temp at the top index of the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
        
            stack.append(i)

        return result
        

        
        