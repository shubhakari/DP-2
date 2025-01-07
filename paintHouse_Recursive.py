class Solution:
    def paintHouse(costs):
        def recurse(costs,house,color,costIncured):
            # base
            if house == len(costs):
                return costIncured
            
            # logic
            if color == 0:
                return min(recurse(costs,house+1,1,costIncured+costs[house][color]),recurse(costs,house+1,2,costIncured+costs[house][color]))
            elif color == 1:
                 return min(recurse(costs,house+1,0,costIncured+costs[house][color]),recurse(costs,house+1,2,costIncured+costs[house][color]))
            else:
                return min(recurse(costs,house+1,0,costIncured+costs[house][color]),recurse(costs,house+1,1,costIncured+costs[house][color]))
                
                
        if costs is None or len(costs) == 0:
            return 0
        costRed = recurse(costs,0,0,0)
        costBlue = recurse(costs,0,1,0)
        costGreen = recurse(costs,0,2,0)
        return min(costRed,min(costBlue,costGreen))
    costs=[[17,2,17],[16,16,5],[14,3,9]]
    print(paintHouse(costs))