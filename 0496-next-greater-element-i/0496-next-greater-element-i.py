class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        
        next_greater = { num:-1 for num in nums2}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack[-1]] = num
                stack.pop()
            stack.append(num)
        for i in range(len(nums1)):
            nums1[i] = next_greater[nums1[i]]
        return nums1