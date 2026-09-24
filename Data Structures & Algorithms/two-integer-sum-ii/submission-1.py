class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # target is the number
        # list is the array of numbers
        first_pointer = 0
        second_pointer = len(numbers)-1
        for num in numbers:
            summation = numbers[first_pointer] + numbers[second_pointer]
            if summation == target:
                return [first_pointer+1, second_pointer+1]
            if summation > target:
                second_pointer -= 1
            if summation < target:
                first_pointer +=1

                
