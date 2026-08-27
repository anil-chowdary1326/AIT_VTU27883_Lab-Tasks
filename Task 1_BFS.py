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
Output:

Enter number of vertices: 5
Enter vertex: A
Enter ajacent vertices separated by space: B C
Enter vertex: B
Enter ajacent vertices separated by space: A D E
Enter vertex: C
Enter ajacent vertices separated by space: A
Enter vertex: D
Enter ajacent vertices separated by space: B
Enter vertex: E
Enter ajacent vertices separated by space: B
Enter starting vertex: A
BFS Traversal: A B C D E 
