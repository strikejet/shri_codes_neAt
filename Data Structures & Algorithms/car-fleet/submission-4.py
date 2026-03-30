class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = dict()
        num = len(position)
        if num == 1:
            return 1
        for i in range(num):
            pos_speed[position[i]] = speed[i]


        position.sort(reverse=True)

        times = [(target - position[i])/pos_speed[position[i]] for i in range(num)]
        cnt = 1
        i, j = 0, 1 
        while i < len(times) and j < len(times):
            if times[i] >= times[j]:
                j = j + 1
            else:
                cnt = cnt + 1
                i = j
                j = j + 1
        return cnt