class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        
        sorted_indices = sorted(range(len(pos)), key=lambda k: -pos[k])
        prev = 0
        fleet = 0

        for i in sorted_indices:
            t = (target - pos[i]) / speed[i]
            if t > prev:
                prev = t
                fleet += 1

        return fleet