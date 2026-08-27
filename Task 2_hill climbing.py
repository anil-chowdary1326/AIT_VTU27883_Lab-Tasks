def hill_climbing(start):
    current = start

    while True:
        # Generate neighboring states
        neighbors = [current - 1, current + 1]

        # Find the best neighbor
        best = max(neighbors)

        print("Current State:", current)
        print("Neighbors:", neighbors)

        # Check whether the neighbor is better
        if best > current and best <= 10:
            current = best
            print("Moving to:", current)
            print()
        else:
            break

    return current


# Starting state
start = 3

# Run Hill Climbing
best_state = hill_climbing(start)

print("Best State Found:", best_state)

Output:
Current State: 3
Neighbors: [2, 4]
Moving to: 4

Current State: 4
Neighbors: [3, 5]
Moving to: 5

Current State: 5
Neighbors: [4, 6]
Moving to: 6

Current State: 6
Neighbors: [5, 7]
Moving to: 7

Current State: 7
Neighbors: [6, 8]
Moving to: 8

Current State: 8
Neighbors: [7, 9]
Moving to: 9

Current State: 9
Neighbors: [8, 10]
Moving to: 10

Current State: 10
Neighbors: [9, 11]
Best State Found: 10
