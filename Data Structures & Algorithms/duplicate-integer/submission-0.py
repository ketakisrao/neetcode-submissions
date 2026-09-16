class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if nums is None:
            # throw error or do something
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True
            nums_dict[num] = True
        return False
        