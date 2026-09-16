class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # can it have negative numbers? yes
        # what do we return if array or target is None? return None

        if nums is None or target is None:
            return None

        n = len(nums)
        l = 0
        h = n - 1

        while l <= h:
            mid = (l + h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return -1
        