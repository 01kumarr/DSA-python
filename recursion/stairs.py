'''
A person can take one step or two step to clim a stair
find the total number of ways, he can clim to top

Hypothesis : here if we know person can clim (n-1) way if he takes one step at a time
             and if a person can clim (n-2) way if he takes two step at a time

             adding both way, we will get total way. why adding? to get the union of ways
'''

def no_of_ways(n:int):
    if (n < 0):
        return 0 # no way to clim as steps are less than zero
    if (n <= 1):
        return 1 # if there is one stair, he can clim using one step so one way, if zero he will not clim so one way

    return no_of_ways(n-1) + no_of_ways(n-2)