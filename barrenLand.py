from itertools import product, izip
import collections


def pair(points):
    p = iter(points)
    return izip(p, p)


def barren_points(barren_edges):
    """
    Parses the barren points input into a list of tuples

    Args:
        param1: (string) A string containing the
        bottom left and top right coordinates

    Returns:
        (list)
    """
    barren_collection = []

    for barren in barren_edges:
        points = []
        for x, y in pair(barren.split()):
            point = (int(x), int(y))

            points.append(point)

        barren_collection.append(points)

    return barren_collection


def neighbors(node):
    """
    Find the points connected to a node

    Args:
        param1: (tuple) The coordinates of the node

    Returns:
        (list)
    """
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


def is_bad(node, bad_edges):
    """
    Check if a node matches barren land

    Args:
        param1 (tuple) The node to check against all barren land
        param2 (list) The list of barren edges

    Returns:
         (bool)
    """
    x = node[0]
    y = node[1]

    for bad in bad_edges:
        p1, p2 = bad

        if x >= p1[0] and x <= p2[0]:
            if y >= p1[1] and y <= p2[1]:
                return 1
    return 0


def bfs(height, width, barren):
    """
    Traverse all coordinates looking for connected components

    Args:
        param1: (int) The height of the graph
        param2: (int) The width of the graph
        param3: (list) The coordinates of the barren land

    Returns:
        (list) A list containing the connected components

    """
    coordinates = list(product(xrange(width), xrange(height)))

    queue = collections.deque()
    visited = set()
    final_collection = []

    for start in coordinates:

        queue.append(start)
        barren_land = []

        while queue:

            node = queue.popleft()

            if not (node[0] >= width or node[1] >= height):
                if node not in visited:
                    new_collection = []
                    visited.add(node)

                    if not is_bad(node, barren):
                        new_collection.append(node)

                    child_nodes = neighbors(node)
                    for child_node in child_nodes:

                        if not is_bad(child_node, barren):
                            queue.append(child_node)

                    if new_collection:
                        barren_land.extend(new_collection)
        if barren_land:
            final_collection.append(barren_land)

    return final_collection


def fertile_land(height, width, barren_edges):

    barren_land = barren_points(barren_edges)

    land = bfs(height, width, barren_land)

    if len(land) == 0:
        return '0'

    total_area = [str(len(area)) for area in land]

    total_area.sort()

    return ' '.join(total_area)