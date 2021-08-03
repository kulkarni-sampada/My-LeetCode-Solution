class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for num in nums :
            diff = target-num
            no_num = nums.copy()
            no_num.remove(num)
            if (diff in no_num) :
                ans.append(nums.index(num))
                if diff == num :
                    ans.append(no_num.index(diff) + 1)
                else :
                    ans.append(nums.index(diff))
                break
        return ans
