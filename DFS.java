n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input("Enter adjacent vertices separated by space: ").split()
    graph[vertex] = neighbours

start = input("Enter starting vertex: ")

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

print("DFS Traversal:", end=" ")
dfs(start)
