class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        @cache
        def get(r,c):
            if c == 0 or r == c:
                return 1

            return get(r-1,c-1) + get(r-1,c)

        ans = [0] * (rowIndex + 1)
        for col in range(rowIndex + 1):
            ans[col] += get(rowIndex,col)
        return ans
         