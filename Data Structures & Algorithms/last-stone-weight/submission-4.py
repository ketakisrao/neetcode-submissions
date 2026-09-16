class Solution:
    # [2,3,6,2,4]
    # [2, 3, 2, 2, 0]
    # [0, 1, 2, 2, 0]
    # [0, 1, 0, 0, 0]
    def get_largest_stones(self, stones: List[int]) -> List[int]:
        first = -1
        second = -1
        first_i = -1
        second_i = -1
        n = len(stones)
        for i in range(0, n):
            if stones[i] == 0:
                continue
            elif stones[i] >= first:
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

    def get_valid_stones_count(self, stones: List[int]) -> int:

        c = 0
        for stone in stones:
            if stone == 0:
                continue
            c += 1
        return c
        
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
            n = self.get_valid_stones_count(stones)
        if n == 1:
            for stone in stones:
                if stone > 0:
                    return stone
        else:
            return 0

