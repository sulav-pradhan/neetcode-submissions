class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        r, l = len(nums)-1, 0
        while l < r: 
            mid = (r + l)//2
            if nums[mid] > nums [r]:
                l = mid + 1
            else:
                r = mid
            res = min(res, nums[r])
        return res

