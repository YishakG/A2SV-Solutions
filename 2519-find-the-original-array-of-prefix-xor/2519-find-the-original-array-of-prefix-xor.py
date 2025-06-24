class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        
        for i in range(1, len(pref)):
            temp = pref[i] ^ pref[i-1]
            arr.append(temp)
        return arr