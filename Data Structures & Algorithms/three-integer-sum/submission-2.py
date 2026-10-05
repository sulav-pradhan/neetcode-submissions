class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array first. 
        nums.sort()
        result = []
        # select a target 
        if len(nums) < 2:
            return []
        for index, num in enumerate(nums): 
            target = -num
            # select left and right pointer
            left = index + 1
            right = len(nums) - 1
           
            while left < right:
                add = nums[left] + nums[right]
                if add == target: 
                    triplet = [num, nums[left], nums[right]]

                    if triplet not in result:
                        result.append(triplet)
                    left += 1
                    right -= 1
                if add > target: 
                    right -= 1
                if add < target: 
                    left += 1
        return result

