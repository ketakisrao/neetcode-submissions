class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n - 1
        # perfectly sorted array
        if nums[l] < nums[h]:
            return nums[0]
        while l < h:
            m = (l + h)//2
            if m - 1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]
            elif nums[0] <= nums[m] and nums[m] >= nums[n-1]:
                l = m + 1
            else:
                h = m - 1
            
        return nums[l]