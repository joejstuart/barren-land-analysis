from itertools import product, izip
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


def pair(points):
    p = iter(points)
    return izip(p, p)


def bad_points(bad_edges):
    bad_collection = []

    for bad in bad_edges:
        points = []
        for x, y in pair(bad.split()):
            points.append([int(x), int(y)])

        bad_collection.extend(points)


    return bad_collection


def n(node):
    x = node[0]
    y = node[1]

    if x == 0 and y == 0:
        return [(x+1, y), (x, y+1)]

    if x > 0 and y == 0:
        return [(x-1, y), (x+1, y), (x, y+1)]

    if x == 0 and y > 0:
        return [(x, y-1), (x+1, y), (x, y+1)]

    if x > 0 and y > 0:
        return [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]


def is_bad(node):
    x = node[0]
    y = node[1]

    for bad in bad_edges:
        p1, p2 = bad

        print p1, p2
        exit()

        if x >= p1 and x+1 <= p2:
            if y >= p1 and y+1 <= p2:
                return 1
    return 0


queue = collections.deque()
visited = set()
#bad_edges = bad_points(['3041', '0012', '1021'])
#bad_edges = bad_points(['0 292 399 307'])
bad_edges = bad_points(['0 0 1 1'])

total_collection = []
final_collection = []

for start in coordinates:

    queue.append(start)

    barren_land = []

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

                if new_collection:
                    total_collection.append(new_collection)
                    barren_land.extend(new_collection)
    if barren_land:
        final_collection.append(barren_land)


print len(total_collection)
print final_collection
print len(final_collection)