print(1)
print(-2)
print(0.22223)
print("hello")
print(6*3)
print(1+2*2*3)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]