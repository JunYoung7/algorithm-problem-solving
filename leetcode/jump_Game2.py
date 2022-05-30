class Solution:
    def jump(self, nums: List[int]) -> int:
        jumpCnt = [0] * len(nums)

        minCanJumpIdx = 1
        maxCanJumpIdx = nums[0]
        preJumpCnt = 0

        nextMinCanJumpIdx = minCanJumpIdx
        nextmaxCanJumpIdx = maxCanJumpIdx

        while (nextMinCanJumpIdx <= len(nums) - 1):
            nextMinCanJumpIdx = maxCanJumpIdx + 1

            for i in range(minCanJumpIdx, maxCanJumpIdx + 1):
                if (i == len(nums) - 1):
                    jumpCnt[i] = preJumpCnt + 1
                    return jumpCnt[-1]
                else:
                    jumpCnt[i] = preJumpCnt + 1
                    nextmaxCanJumpIdx = max(nextmaxCanJumpIdx, i + nums[i])

            preJumpCnt += 1

            maxCanJumpIdx = nextmaxCanJumpIdx

        return jumpCnt[-1]

