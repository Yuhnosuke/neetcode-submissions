class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p, s))
        cars.sort(key=lambda x: x[0], reverse=True)

        times = []
        
        for p, s in cars:
            time = (target - p) / s
            
    
            if not times or times[-1] < time:
                times.append(time)
        
        return len(times)
        
        