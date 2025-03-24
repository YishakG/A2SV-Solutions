class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        arr = 1 2 3
        k = 2

        path = [1, 2, 3]
                                         []
                
                         [1]                            []

                   [1, 2]   [1]                   [2]        []

    [1, 2, 3]  [1, 2]       [1, 3] [1]         [2, 3] [2]  [3]   []





        """
        ans = []
        def bt(idx, path):

            if len(path) == k:
                ans.append(path)
                return

            if idx == n + 1:
                return

            bt(idx + 1, path[:] + [idx])
            bt(idx + 1, path[:])

            return

        bt(1, [])

        return ans
