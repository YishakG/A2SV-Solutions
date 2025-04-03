class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        temp = set()
        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                ans.append(num)
        return ans
