class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
         
        for i in range(len(nums)):
            
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_numbers.append(i + 1)

        return missing_numbers
