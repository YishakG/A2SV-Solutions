class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
            happiness.sort(reverse=True)   
            max_sum = 0
            
            for i in range(k):
                adjusted_happiness = max(0, happiness[i] - i)   
                max_sum += adjusted_happiness

                if adjusted_happiness == 0:   
                    break

            return max_sum