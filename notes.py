""" 
Sample Input: 
v e time cost start
3 2 3000    2     0

coordinates of points, to be ignored: 
    48.8582             2.2945
    50.0                3.09
    51.424242           3.02
    
start, end, direction, cost, length
0       1      1        30      250
1       2      2        45      200 
"""

"""
0 -> 2, 3, 4               -> adj_list
0 -> cost(2), cost(3)

dual -> 

2 -> 5, 6

(2, cost(2), path(2), True/False)

vertex start -> struct Edge {
    vertex end
    bool is_visited
    int direction
    int cost
    int length
    int length/cost
}


adj_list = []

0 -> (2,cost, path, direction), (3, ...) :checkbox: 
1 -> (..), ...
2 -> 

street

>>> mylist = [(2,3), (3,3)]
>>> [a for (a, p) in mylist if p == 3]
[2, 3]

"""

"""
Rules for every question:

Step 1: Decide data structure to use (input format) -> class, tuple
Step 2: Parts:
        => Parse Input
        => Solve 
        => Score (judge.cpp)
        => Output format (as asked)
Step 3: Submit a low score solution to get a score
        => Input Working :checkbox:
        => Output Working :checkbox:
        => Basic solution working :checkbox:
Step 4: Improvements
"""


"""
Score #1: 3318 (length/cost)
Score #2: 3416 (length)

"""


   # for _ in range(v):
   #     adj_list.append([])
#     cost_list.append([])
#     length_list.append([])
#     dual.append([])
#     visited_list.append([])
#     length_per_cost.append([])

# for i in range(e):
#     a, b, d, c, l = i.readline().split()
#     # adjacency list is a way to represent graph and to store edges and vertices
#     adj_list[a].append(b) # a -> b , this b for this a, stored in an adjacency list
#     cost_list[a].append(c) # a -> c
#     length_list[a].append(l) # a -> l
#     visited_list[a].append(False)
#     length_per_cost[a].append(l/c)

#     if d==1: # unidirectional, only path from a is possible, a -> b, not a <-> b
#         dual[a].append(False) # path from b -> a is false and a -> is true

#     if d == 2: # bidirection, a and b both are true
#         adj_list[b].append(a) # b -> a , i.e. a is reachable from b
#         cost_list[b].append(c) # b -> c
#         length_list[b].append(l) # b -> l
#         dual[a].append(True) # path from b -> a is true
#         dual[b].append(True)  # path from a -> b is true
#         visited_list[b].append(False)
#         length_per_cost[b].append(l/c)


# adj_list = [] # a, b
# cost_list = [] # a, b, c   cost_list[a][adj_list[a].index(b)] == c
# length_list = [] # a, b, l
# dual = [] # a, b direction
# visited_list = [] # a, b, visited  visited_list[a][adj_list[a].index(b)]  == True if visited else False
# length_per_cost = []
