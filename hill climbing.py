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
