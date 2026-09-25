class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I need prefix product and suffix product   
        prefix, suffix, product_not_self = [], [], []
        # first create prefix
        init = 1
        for num in nums: 
            prefix.append(init)
            init *= num
        init = 1
        for num in list(reversed(nums)):
            suffix.append(init)
            init *= num
        suffix.reverse()


        for k in range(0, len(nums)):
             product = prefix[k] * suffix[k]
             product_not_self.append(product)

        return product_not_self
        

        
        