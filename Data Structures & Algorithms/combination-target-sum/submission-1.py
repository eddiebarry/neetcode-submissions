class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = {}

        def calc_sub(i, tg):            
            k = (i,tg)
            # print(k)

            if k in dp:
                return dp[k]
            
            elif tg == 0:
                return [[]]
            elif i == len(nums):
                return None

            ans = []
            if nums[i] <= tg:
                # what if we use nums i
                t = calc_sub(i, tg-nums[i])
                for temp_sub_ans in t if t else []:
                    ans.append([nums[i]] +temp_sub_ans)

                # what if we dont
                t = calc_sub(i+1, tg)
                ans += t if t else []                
            else:
                ans = calc_sub(i+1,tg)
                
            dp[k]=ans
            return ans

        return calc_sub(0, target)