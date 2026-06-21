class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time = [(position[i], (target-position[i])/speed[i]) for i in range(len(position))]
        time = sorted(time, key=lambda x:-x[0])
        for position, time in time:
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)