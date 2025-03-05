class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        one = "1" * (count["1"]-1)
        zero = "0" * (count["0"])
        return one + zero + "1"
        