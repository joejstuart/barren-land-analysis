from itertools import product
import collections


dim_x = 6
dim_y = 5

coordinates = list(product(xrange(dim_x), xrange(dim_y)))

matrix = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]


def bad_points(bad_edges):
    bad_collection = []

    for bad in bad_edges:
        x = bad[:2]
        y = bad[2:4]

        p1 = (int(x[0]), int(x[1]))
        p2 = (int(y[0]), int(y[1]))

        bad_collection.append([p1, p2])

    return bad_collection


def n(node):
    x = node[0]
    y = node[1]

    return [(x+1, y), (x, y+1), (x+1, y+1)]


def is_bad(node):
    x = node[0]
    y = node[1]

    for bad in bad_edges:
        p1, p2 = bad

        if x >= p1[0] and x+1 <= p2[0]:
            if y >= p1[1] and y+1 <= p2[1]:
                return 1
    return 0


queue = collections.deque()
visited = set()
bad_edges = bad_points(['3041', '0012', '1021'])

total_collection = []

for start in coordinates:

    queue.append(start)

    while queue:

        node = queue.popleft()

        if not (node[0] >= dim_x or node[1] >= dim_y):

            if node not in visited:

                new_collection = []

                visited.add(node)

                child_nodes = n(node)

                if not is_bad(node):
                    new_collection.append(node)

                for child_node in child_nodes:

                    if not is_bad(node):
                        queue.append(child_node)
                        new_collection.append(child_node)

                if new_collection:
                    total_collection.append(new_collection)


print len(total_collection)
print total_collection