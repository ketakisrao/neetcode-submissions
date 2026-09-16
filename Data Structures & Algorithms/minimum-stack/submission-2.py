class MinStack:

    def __init__(self):
        self.min = []
        self.nums = []
        self.tos = -1
        
# min = [1, 1, 0]
# nums = [1, 2, 0]
# tos = 2
# val = 0
    def push(self, val: int) -> None:
        self.nums.append(val)
        self.tos +=1
        if self.tos > 0:
            if self.tos < len(self.min):
                self.min[self.tos] = min(val, self.min[self.tos - 1])
            else:
                self.min.append(min(val, self.min[self.tos - 1]))
        else:
            self.min = [val]

    def pop(self) -> None:
        popped_num = self.nums.pop()
        self.tos -= 1
        

    def top(self) -> int:
        return self.nums[self.tos]

    def getMin(self) -> int:
        return self.min[self.tos]
