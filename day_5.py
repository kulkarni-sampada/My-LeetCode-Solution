class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        Alex_max_sum = []
        Lee_max_sum = 0
        original_piles_len = len(piles)
        for stone in piles :
            maxValue = max(piles)
            Alex_max_sum.append(maxValue)
            piles.remove(maxValue)
            piles_len = len(piles)
            if piles_len == original_piles_len - 2 :
                break
        Lee_max_sum = max(piles) + Alex_max_sum[0]
        print(Lee_max_sum)
        print(sum(Alex_max_sum))
        if sum(Alex_max_sum) >= Lee_max_sum :
            return True
        else :
            return False
