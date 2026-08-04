class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        start = nums[0]
        end = nums[-1]
        ans = []
        
        j = 0
        for i in range(start, end + 1):
            if j < len(nums) and nums[j] == i:
                j += 1
            else:
                ans.append(i)
                
        return ans