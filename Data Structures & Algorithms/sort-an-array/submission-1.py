class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(n: int, i: int):
            """
            Iterative heapify ensures absolute O(1) space complexity by avoiding 
            the call-stack overhead of recursion.
            """
            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                # Check if the left child exists and is greater than the parent
                if left < n and nums[left] > nums[largest]:
                    largest = left

                # Check if the right child exists and is greater than the current largest
                if right < n and nums[right] > nums[largest]:
                    largest = right

                # If a child is larger, swap and update pointer to continue sifting down
                if largest != i:
                    nums[i], nums[largest] = nums[largest], nums[i]
                    i = largest
                else:
                    break  # Element is in its correct Max-Heap position

        n = len(nums)

        # Step 1: Build the Max-Heap from the bottom up
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Step 2: Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            # Swap the current absolute maximum (at index 0) with the end of the unsorted boundary
            nums[0], nums[i] = nums[i], nums[0]
            
            # Restore the Max-Heap property on the remaining unsorted elements
            heapify(i, 0)

        return nums
        