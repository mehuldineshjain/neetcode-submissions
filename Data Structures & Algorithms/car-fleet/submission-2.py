class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time_formula = (target - position) / speed
        # If I determine the time taken by all cars,
        # The car at the last position generally defines the previous car time
        # If the front car has not reached the destination then the car has to join
        # Let us sort the positions first

        # 1. Pair each value with its original index
        indexed_position = list(enumerate(position))
        # Result: [(0, 40), (1, 10), (2, 30), (3, 20)]

        # 2. Sort based on the values (the second element of each tuple)
        sorted_position = sorted(indexed_position, key=lambda x: x[1], reverse=True)
        # Result: [(1, 10), (2, 20), (3, 30), (0, 40)]

        
        time = []
        for i,p in sorted_position:
            time.append(((target - p) / speed[i]))
        highest_time = 0
        fleets = 0
        for i in range(len(time)):
            if time[i] > highest_time:
                fleets += 1
                highest_time = time[i]

        return fleets



