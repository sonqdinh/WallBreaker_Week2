class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             while nums[i] != nums[nums[i] - 1]:
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
            
#         ans = []
#         for i in range(len(nums)):
#             if nums[i] != i + 1:
#                 ans.append(nums[i])
#                 ans.append(i + 1)
        
#         return ans
        ans = []
        setNumbs = set()
        for n in nums:
            if n in setNumbs:
                ans.append(n)
            else:
                setNumbs.add(n)
        
        for n in range(1, len(nums) + 1):
            if n not in setNumbs:
                ans.append(n)
                return ans
                