from collections import deque

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input("Enter ajacent vertices separated by space: ").split()
    graph[vertex] = neighbours

start = input("Enter starting vertex: ")

visited = set()
queue = deque([start])
visited.add(start)

print("BFS Traversal:", end=" ")

while queue:
    vertex = queue.popleft()
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
