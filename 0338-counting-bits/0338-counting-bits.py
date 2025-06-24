class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0,n+1):
            temp = str(bin(i))
            ans.append(temp.count("1"))
        return ans

        