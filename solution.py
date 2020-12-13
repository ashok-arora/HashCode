import sys
from parse import *
from output import *
from basicGreedy import *
from greedyLookahead import *

# TODO:
# Convert bidirectional edges to 2 unidirectional edges by:
# if Edge.direction == 2, then Edge.is_visited == True and Edge_2nd.is_visited == True
# map banaae a, street and if bi-dirctional insert in map b, street (rm -rf */ this line for now)


def main():
    start, cars, time, class_adj_list = parse("in.txt")
    cars_data = car_start(start, cars, time, class_adj_list)
    # print_solution(cars_data, cars, 'basic_greedy')
    cars_data = car_start_look_ahead(start, cars, time, class_adj_list)
    print_solution(cars_data, cars, 'greedy_look_ahead')


if __name__ == "__main__":
    main()
