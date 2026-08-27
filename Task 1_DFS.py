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

Output:

Enter number of vertices: 5
Enter vertex: A
Enter adjacent vertices separated by space: B C
Enter vertex: B
Enter adjacent vertices separated by space: A D E
Enter vertex: C
Enter adjacent vertices separated by space: A
Enter vertex: D
Enter adjacent vertices separated by space: B
Enter vertex: E
Enter adjacent vertices separated by space: B
Enter starting vertex: A
DFS Traversal: A B D E C 
