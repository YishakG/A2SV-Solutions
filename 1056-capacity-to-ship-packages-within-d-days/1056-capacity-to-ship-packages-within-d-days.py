class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:  
            mid = (left + right) // 2
            curr_days = 1  
            curr_sum = 0
                        
            for weight in weights:
                if curr_sum + weight > mid:
                    curr_days += 1
                    curr_sum = weight
                else:
                    curr_sum += weight
            
                  
            if curr_days > days:   
                left = mid + 1
            else:   
                right = mid
                
        return right