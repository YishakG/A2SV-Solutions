class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = defaultdict(int)
        def get(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if c == 0 or r == c:
                return 1

            memo[(r,c)] = get(r-1,c-1) + get(r-1,c)
            return memo[(r,c)]

        ans = [0] * (rowIndex + 1)
        for col in range(rowIndex + 1):
            ans[col] += get(rowIndex,col)
        return ans
         