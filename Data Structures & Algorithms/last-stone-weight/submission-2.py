class Solution:

    def get_largest_stones(self, stones: List[int]) -> List[int]:
        first = -1
        second = -1
        first_i = -1
        second_i = -1
        n = len(stones)
        for i in range(0, n):
            if stones[i] >= first:
                second = first
                second_i = first_i
                first = stones[i]
                first_i = i
            elif stones[i] > second:
                second = stones[i]
                second_i = i
        return [first_i, second_i]

    def remove_empty_stones(self, stones: List[int]):
        n = len(stones)
        i = 0
        while i < n:
            if stones[n - i - 1] == 0:
                stones.pop(n - i - 1)
                n -= 1
            else:
                i += 1
        
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones is None:
            return 0

        n = len(stones)

        while n > 1:
            largest_stones = self.get_largest_stones(stones)
            print(largest_stones)
            largest = stones[largest_stones[0]]
            second_largest = stones[largest_stones[1]]
            stones[largest_stones[0]] = largest - second_largest
            stones[largest_stones[1]] = 0
            self.remove_empty_stones(stones)
            n = len(stones)
            
        if stones:
            return stones[0]
        else:
            return 0

