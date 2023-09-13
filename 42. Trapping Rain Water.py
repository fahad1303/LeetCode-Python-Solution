def trap(self, height: List[int]) -> int:
        trap_unit = 0
        lr_list = []
        rl_list =[]
        lr_max = rl_max =0
        for x in range(0,len(height)):
            if height[x]> lr_max:
                lr_max = height[x]
            lr_list.append(lr_max)
        print(lr_list)
        for x in reversed (range(0,len(height))):
            if height[x] > rl_max:
                rl_max = height[x]
            rl_list.insert(0,rl_max)
        print(rl_list)
        for x in range(0,len(height)):
            temp1 = lr_list[x]
            temp2 = rl_list[x]
            minof = min(temp1,temp2)
            trap_unit = trap_unit + (minof -height[x] )
        return trap_unit
