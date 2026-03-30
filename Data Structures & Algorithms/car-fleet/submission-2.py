class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = dict()

        for i in range(len(position)):
            pos_speed[position[i]] = speed[i]
        if len(position) == 1:
            return 1


        position.sort(reverse=True)
        speed_2 = [None] * len(speed)
        for p in pos_speed.keys():
            ind = position.index(p)
            speed_2[ind] = pos_speed[p]

        times = [(target - position[i])/speed_2[i] for i in range(len(position))]
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