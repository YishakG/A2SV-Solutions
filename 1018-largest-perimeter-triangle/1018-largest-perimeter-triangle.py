class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        the sum of the two smallest sides should be greater than the largest side
        
        """
        nums.sort(reverse = True)
        # l , r = len(nums) - 3 , -1
        # while l >= 0:
        #     if nums[l] + nums[l+1] > nums[r]:
        #         return nums[l] + nums[l+1] + nums[r]
        #     else:
        #         r -= 1
        #     l -= 1
        # return 0
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
