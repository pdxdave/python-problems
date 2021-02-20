'''
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

Note: for each additional number to n, it increases the area by 4.
For instance, n=1 returns an area of 1. n=2 returns an area of 5.         
n=3 returns an area of 13. The below calculation returns that.

                *           *
     *        * * *       * * *    
    n=1         *       * * * * *
                n=2       * * *
                            *
                            n=3
'''

def shapeArea(n):
    return n * n + (n-1)**2 