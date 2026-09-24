class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is the frequency and the value is the list if the list contains 2 element then reutn eslse return the two top list 
        # how to crerate a list then 
        # length of an array 0 to length of array where all the values are empty array 
        # check for empty array take the top populated array 
        # first create an empty hashmap 
        len_nums = len(nums)
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        # create a bucket
        bucket = [[] for i in range(len_nums+1)]
        # add to bucket 
        # based on the frequency I need to add to the bucket so go through the frequency freq_map if key exist append to the bucket
        for key, value in freq_map.items():
            bucket[value].append(key)
        # now that it is populated I need to return it the top k elemnts 
        # if len last item in array whose len = k return that esle add the list in descending order untill the length of new list is = k so I don't need to check I just add all the items in descending order to the list and retrun as soon as the length is equal to the k 
        answer = []
        for arr in range(len(bucket) - 1, 0, -1):
            answer.extend(bucket[arr])

            if len(answer) >= k:
                return answer[:k]

        return answer

