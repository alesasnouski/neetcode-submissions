from typing import List
import math

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        hops = []
        st = []
 
        for i in range(len(position)):
            h = (target - position[i]) / speed[i]
            hops = [(h, position[i])] + hops
        
        hops.sort(key=lambda x: x[1])

        print(hops)

        while len(hops) > 0:
            tl = hops.pop()
            if len(st) == 0:
                st.append(tl)
            else:
                if tl[0] > st[-1][0]:
                    st.append(tl)    

        return len(st) 