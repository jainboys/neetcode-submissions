class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        time = [(position[i], (target-position[i])/speed[i]) for i in range(len(position))]
        time = sorted(time, key=lambda x:-x[0])
        for position, time in time:
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        return len(fleets)