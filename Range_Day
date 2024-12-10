SIZE = 5

# Initialize the matrix and other variables
matrix = []
targets = 0
my_position = []

# Read the matrix and find Alice's position and targets
for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

# Directions for movement
direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

targets_down = []  # To keep track of the positions of the targets that are hit

# Number of commands to process
N = int(input())

# Process each command
for _ in range(N):
    command = input().split()

    if command[0] == "shoot":
        # Determine the direction of the shot
        row = my_position[0]
        col = my_position[1]

        # Determine the shooting direction
        dr, dc = direction[command[1]]
        
        # Move step by step in the given direction to find the first target
        while 0 <= row < SIZE and 0 <= col < SIZE:
            row += dr
            col += dc
            
            if 0 <= row < SIZE and 0 <= col < SIZE:
                if matrix[row][col] == "x":
                    matrix[row][col] = "."  # Mark the target as hit
                    targets -= 1
                    targets_down.append([row, col])  # Record the target position
                    break
        
        # Check if all targets are hit, and end the program if they are
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == "move":
        # Determine the movement direction
        dr, dc = direction[command[1]]
        steps = int(command[2])

        # Try to move Alice in the given direction
        for _ in range(steps):
            new_row = my_position[0] + dr
            new_col = my_position[1] + dc
            
            if 0 <= new_row < SIZE and 0 <= new_col < SIZE and matrix[new_row][new_col] == ".":
                # Move Alice if the new position is empty
                matrix[my_position[0]][my_position[1]] = "."
                my_position = [new_row, new_col]
                matrix[new_row][new_col] = "A"
            else:
                # Stop if the new position is invalid (either out of bounds or blocked)
                break

# After processing all commands, check if there are still targets left
if targets > 0:
    print(f"Training not completed! {targets} targets left.")

# Print the positions of the targets that were hit
for target in targets_down:
    print(f"[{target[0]}, {target[1]}]")
