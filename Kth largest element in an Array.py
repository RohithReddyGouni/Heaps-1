class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        length=len(nums)
        for i in range(length):
            if len(minHeap)<k:
                heappush(minHeap,nums[i])
            else:
                popFirst=minHeap[0]
                if popFirst<nums[i]:
                    heappop(minHeap)
                    heappush(minHeap,nums[i])
       
        return minHeap[0]