import collections


matrix = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]


def neighbors(node, queue):
    x = node[0]
    y = node[1]

    queue.append((x+1, y))
    queue.append((x, y+1))
    queue.append((x+1, y+1))

    return queue


def n(node):
    x = node[0]
    y = node[1]

    return [(x+1, y), (x, y+1), (x+1, y+1)]


queue = collections.deque()
queue.append((0, 0))
visited = set()
bad_queue = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)]
components = []
area = 0

while queue:

    node = queue.popleft()

    if node[0] <= 6 and node[1] <= 6 and node not in visited:

        visited.add(node)

        for child_node in n(node):

            visited.add(child_node)
            queue = neighbors(child_node, queue)
            components.append(child_node)

        if node not in bad_queue:
            components.append(node)
            area += 1

print len(components)
print area
print components
for bad in bad_queue:
    if bad in components:
        print 'bad'