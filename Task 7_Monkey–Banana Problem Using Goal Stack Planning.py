# Monkey-Banana Problem using Goal Stack Planning

def monkey_banana():
    # Initial state
    monkey_pos = "window"
    box_pos = "window"
    banana_pos = "center"
    on_box = False
    has_banana = False

    goal = "Monkey has banana"

    print("Initial State:")
    print(f"Monkey position : {monkey_pos}")
    print(f"Box position    : {box_pos}")
    print(f"Banana position : {banana_pos}")
    print(f"Monkey on box   : {on_box}")
    print(f"Has banana      : {has_banana}")

    print("\nGoal:", goal)
    print("\n--- Goal Stack Planning ---")

    # Step 1: Monkey walks to the box
    if monkey_pos != box_pos:
        monkey_pos = box_pos

    print("1. Monkey walks to the box")

    # Step 2: Push box to banana position
    if monkey_pos == box_pos:
        box_pos = banana_pos
        monkey_pos = banana_pos

    print("2. Monkey pushes the box under the banana")

    # Step 3: Climb the box
    if monkey_pos == box_pos:
        on_box = True

    print("3. Monkey climbs onto the box")

    # Step 4: Grasp banana
    if on_box and box_pos == banana_pos:
        has_banana = True

    print("4. Monkey grasps the banana")

    # Final state
    print("\nFinal State:")
    print(f"Monkey position : {monkey_pos}")
    print(f"Box position    : {box_pos}")
    print(f"Banana position : {banana_pos}")
    print(f"Monkey on box   : {on_box}")
    print(f"Has banana      : {has_banana}")

    if has_banana:
        print("\nGoal Achieved: Monkey has the banana!")
    else:
        print("\nGoal Failed")


# Run the program
monkey_banana()

Output:
Initial State:
Monkey position : window
Box position    : window
Banana position : center
Monkey on box   : False
Has banana      : False

Goal: Monkey has banana

--- Goal Stack Planning ---
1. Monkey walks to the box
2. Monkey pushes the box under the banana
3. Monkey climbs onto the box
4. Monkey grasps the banana

Final State:
Monkey position : center
Box position    : center
Banana position : center
Monkey on box   : True
Has banana      : True

Goal Achieved: Monkey has the banana!
