class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_state = [] # (position, speed)
        for p, s in zip(position, speed):
            car_state.append((p, s))
        car_state.sort(reverse=True)

        times = []
        for p, s in car_state:
            time = (target - p) / s
            if not times:
                times.append(time)
            if times and times[-1] < time:
                times.append(time)
        return len(times)
        
        