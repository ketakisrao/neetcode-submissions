class KthLargest:

    pos = 0
    nums = []

    def __init__(self, k: int, nums: List[int]):
        self.pos = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.pos]
        
