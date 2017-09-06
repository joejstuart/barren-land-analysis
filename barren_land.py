import collections


queue = collections.deque()
queue.append((0, 0))
visited = set()
bad_queue = [(10, 5), (10, 6), (11, 6), (10, 6)]

def neighbors(node, queue):
    x = node[0]
    y = node[1]

    queue.append((x+1, y))
    queue.append((x, y+1))
    queue.append((x+1, y+1))

    return queue


components = []

while queue:

    node = queue.popleft()

    if node not in bad_queue and node[0] <= 399 and node[1] <= 599 and node not in visited:

        visited.add(node)
        queue = neighbors(node, queue)
        components.append(node)

for bad in bad_queue:
    if bad in components:
        print 'bad'