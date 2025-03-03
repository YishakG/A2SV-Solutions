class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        the sum of the two smallest sides should be greater than the largest side
        
        """
        nums.sort()
        l , r = len(nums) - 3 , -1
        while l >= 0:
            if nums[l] + nums[l+1] > nums[r]:
                return nums[l] + nums[l+1] + nums[r]
            else:
                r -= 1
            l -= 1
        return 0
