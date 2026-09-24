class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # value -> first index we saw it

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                # indices[diff] is an earlier index, i is the current index
                return [indices[diff], i]
            # only store the first occurrence
            if n not in indices:
                indices[n] = i

        raise ValueError("No solution")
        