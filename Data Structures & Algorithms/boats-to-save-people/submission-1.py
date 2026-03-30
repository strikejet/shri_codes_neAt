class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people) - 1
        boat_count = 0
        people.sort()
        while left <= right:
            if people[right] + people[left] <= limit:
                left = left + 1
                     
            right = right - 1
            boat_count = boat_count + 1
        
        return boat_count
