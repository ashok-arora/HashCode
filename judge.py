"""
To check your score, enter the below in a terminal window:

python3 judge.py <input_file_path> <output_file_path>
"""

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as inp:
    vertices, edges, tot_time, cars, source = map(int, inp.readline().split())

    for _ in range(vertices):
        inp.readline()

    adj_list = []
    cost_list = []
    path_list = []
    dual = []
    for _ in range(vertices):
        adj_list.append([])
        cost_list.append([])
        path_list.append([])
        dual.append([])

    for _ in range(edges):
        a, b, d, c, l = map(int, inp.readline().split())
        if (d == 2):
            adj_list[b].append(a)
            cost_list[b].append(c)
            path_list[b].append(l)
            dual[b].append(True)
            dual[a].append(True)
        adj_list[a].append(b)
        cost_list[a].append(c)
        path_list[a].append(l)
        if (d == 1):
            dual[a].append(False)

tot_length_traversed = 0
with open(output_file, 'r') as out:
    out_cars = int(out.readline())
    assert cars == out_cars, "The number of cars do not match input."
    for _ in range(cars):
        time_left = tot_time
        vertices_visit = int(out.readline())
        present_node = int(out.readline())
        assert present_node == source, "First node of each car should be the source node."
        for _ in range(vertices_visit - 1):
            next_node = int(out.readline())
            assert next_node in adj_list[present_node], "Node cannot be reached."
            index = adj_list[present_node].index(next_node)
            assert cost_list[present_node][index] <= time_left, "Time taken by car is more than the available time."
            tot_length_traversed += path_list[present_node][index]
            time_left -= cost_list[present_node][index]
            path_list[present_node][index] = 0
            if dual[present_node][index]:
                index_2 = adj_list[next_node].index(present_node)
                path_list[next_node][index_2] = 0
            present_node = next_node


print("Score: {}".format(tot_length_traversed))
