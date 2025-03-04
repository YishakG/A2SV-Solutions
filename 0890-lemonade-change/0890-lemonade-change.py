class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = ten_count = 0
        for bill in bills:
            if bill == 5:
                five_count += 1
            elif bill == 10:
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1
            elif bill == 20:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    five_count -= 3
                else:
                    return False
        return True
        # no need of dictionary
        # no need of keeping track of the 20
        # 
        # moneys = {5:0,10:0,20:0}
        # for bill in bills:
        #     moneys[bill] += 1
        #     change = bill - 5
        #     if change == 5:
        #         if moneys[5] < 1:
        #             return False
        #         else:
        #             moneys[5] -= 1
        #     elif change == 15:
        #         if moneys[5] >= 1 and moneys[10] >= 1:
        #             moneys[5] -= 1
        #             moneys[10] -= 1
        #         elif moneys[5] >= 3:
        #             moneys[5] -= 3
        #         else:
        #             return False
        # return True



        
        