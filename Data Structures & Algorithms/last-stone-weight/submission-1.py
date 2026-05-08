class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            heaviest = stones.pop()
            second = stones.pop()
            if heaviest != second:
                stones.append(heaviest-second)
        if stones:
            return stones[0]
        return 0

        


        