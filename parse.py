class Edge:

    def __init__(self, start, end, cost, length, direction):
        self.start = start
        self.end = end
        self.cost = cost
        self.length = length
        self.direction = direction
        self.is_visited = False
        self.length_by_cost = length/cost


# making global variables


def parse(file):
    i = open(file, "r")
    v, e, time, cars, start = map(int, i.readline().split())
    for _ in range(v):
        i.readline()

    # 0 -> 2, 3, 4 -> adj_list
    # 0 ->   0, 1, 2  (indexes) cost[0][0.(1)] = cost from 0 to 3


    class_adj_list = []
    for _ in range(v):
        class_adj_list.append([])

    for _ in range(e):
        a, b, d, c, l = map(int, i.readline().split())
        class_adj_list[a].append(Edge(a, b, c, l, d))
        if d == 2:
            class_adj_list[b].append(Edge(b, a, c, l, d))

    return start, cars, time, class_adj_list


if __name__ == "__main__":
    parse()
