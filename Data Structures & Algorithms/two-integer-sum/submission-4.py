class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d: dict[int, int] = {}
        for i in range(len(nums)):
            cur: int = nums[i]
            addend: int = target - cur
            if addend in d:
                return [d[addend], i]
            d[cur] = i
        