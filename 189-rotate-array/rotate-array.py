class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n  
        temp = []
        for i in range(n - k):
            temp.append(nums[i]) 
        for i in range(k):
            nums[i] = nums[n - k + i]
        for i in range(n - k):
            nums[k + i] = temp[i]