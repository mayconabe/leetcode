class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []

        for i in range(len(nums)):

            complemento = target - nums[i]

            if complemento in nums:
                if nums.index(complemento) != i:
                    lst.append(i)
                    lst.append(nums.index(complemento))
                    break
        return lst
