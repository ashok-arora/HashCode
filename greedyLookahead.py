from parse import *

def car_start_look_ahead(start, cars, time, class_adj_list):
    iter_count = 17
    cars_data = []
    for car in range(cars):
        cars_data.append([start])
        max_sum = 0
        time_left = time
        current_node = start
        while time_left > 0:
            for edge in class_adj_list[current_node]:
                sum_of_iter_costs = 0
                guess_node = current_node
                visited = []
                time_left_guess = time_left
                # source -> possibility 1
                # after possibility 1's iter steps:
                #   current_node = start
                #   time_left = initial_time = time
                for _ in range(iter_count):
                    while sum_of_iter_costs < time_left:
                        cost, node, edge = findGreedyandReturnCost(guess_node, time_left, class_adj_list)
                        if cost==-1:
                            break
                        else:
                            sum_of_iter_costs += cost
                            guess_node = node
                            visited.append(edge)
                            time_left_guess -= cost
                if sum_of_iter_costs > max_sum:
                    max_sum = sum_of_iter_costs
                    for node in visited:
                        cars_data[car].append(node.start)
                        node.is_visited = True
                        if node.direction == 2:
                            for nextEdg in class_adj_list[node.end]:
                                if nextEdg.end == node.start:        # node.start (aniket) + +1
                                    nextEdg.is_visited = True
                                    break
                    # for node in range(len(visited) -1):
                    #     for a in range(len(class_adj_list[node])):
                    #         if node.end == class_adj_list[node][a].start:
                    #             class_adj_list[node][a].visited = True
                    #             if class_adj_list[node][a].direction == 2:
                    #                 class_adj_list[a][node].visited = False
                                
                else:
                    visited = []
                # move in that direction and mark is_visited for iter_count
				# for i in range(iter_count):
				# 	chain -> a -> b -> c
				# 		
    return cars_data

# greedy Node functions
def findGreedyandReturnCost(current_pos, time_left, class_adj_list):
    maxDisPerCost, maxIdx = 0, -1
    tLeft = -1
    cost = 0
    best_possible_edge = Edge(1,1,1,1,1)
    for ed in class_adj_list[current_pos]:
        if (ed.is_visited == False) and (ed.cost <= time_left) and (ed.length > maxDisPerCost):
            maxDisPerCost = ed.length
            maxIdx = ed.end
            tLeft = time_left - ed.cost
            best_possible_edge = ed
			# ed.is_visited = True
            cost = ed.cost
            # if ed.direction == 2:
            #     for anotherEdge in class_adj_list[ed.end]:
            #         if anotherEdge.end == current_pos:
            #             anotherEdge.is_visited = True
            #             break

    if maxIdx != -1:
        return cost, maxIdx, ed

    return -1, -1, -1

    
