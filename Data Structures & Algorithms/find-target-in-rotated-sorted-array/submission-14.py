class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n - 1
        if nums[l] == target:
            return l
        if nums[h] == target:
            return h

        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            if nums[0] <= nums[m]:
                #left is sorted
                if target >= nums[0] and target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                #right is sorted
                if target > nums[m] and target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        return -1