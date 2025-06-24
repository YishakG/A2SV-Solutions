class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1,n+1):
            # The number of 1 in i equals number of 1's in i//2 plus the last bit
            # O(n) Time Complexity O(1) space complexity
            ans[i] = ans[ i >> 1] + (i & 1)
        return ans 
        #Not efficient for large numbers
        # ans = []
        # for i in range(0,n+1):
        #     temp = str(bin(i))
        #     ans.append(temp.count("1"))
        # return ans

        