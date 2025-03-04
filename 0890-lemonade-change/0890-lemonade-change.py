class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        moneys = {5:0,10:0,20:0}
        for bill in bills:
            moneys[bill] += 1
            change = bill - 5
            if change == 5:
                if moneys[5] < 1:
                    return False
                else:
                    moneys[5] -= 1
            elif change == 15:
                if moneys[5] >= 1 and moneys[10] >= 1:
                    moneys[5] -= 1
                    moneys[10] -= 1
                elif moneys[5] >= 3:
                    moneys[5] -= 3
                else:
                    return False
        return True



        
        