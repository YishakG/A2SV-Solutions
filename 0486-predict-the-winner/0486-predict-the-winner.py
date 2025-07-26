class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def play(left, right):
            # base case 
            if left == right:
                return nums[left]
            # current Player 1 picks Left or Right then Player 2 picks Right or Left respectively
            pickLeft = nums[left] - play(left + 1, right)
            pickRight = nums[right] - play(left, right - 1)
            
            return max(pickLeft,pickRight)
        
        return play(0,len(nums)-1) >= 0