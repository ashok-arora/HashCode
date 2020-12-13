def car_start(start, cars, time, class_adj_list):
    cars_data = []
    for car in range(cars):
        cars_data.append([start])
        current_pos = start
        time_left = time
        # next_pos = []
        while time_left > 0:
            next_pos = findGreedyNode(current_pos, time_left, class_adj_list)     # returns a tuple (pos, time_left)
            if next_pos[0] == -1: # no best node found ?
                break
            else:
                current_pos = next_pos[0]
                time_left = next_pos[1]
            cars_data[car].append(next_pos[0])

    return cars_data

#greedy Node functions
def findGreedyNode(current_pos, time_left, class_adj_list):

    maxDisPerCost, maxIdx = 0, -1
    tLeft = -1

    for ed in class_adj_list[current_pos]:
        if (ed.is_visited == False) and (ed.cost <= time_left) and (ed.length > maxDisPerCost):
            maxDisPerCost = ed.length
            maxIdx = ed.end
            tLeft = time_left - ed.cost
            ed.is_visited = True
            if ed.direction == 2:
                for anotherEdge in class_adj_list[ed.end]:
                    if anotherEdge.end == current_pos:
                        anotherEdge.is_visited = True
                        break

    if maxIdx != -1:
        return maxIdx, tLeft
    
    return -1, -1