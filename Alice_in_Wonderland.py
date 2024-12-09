n = int(input())

matrix = []

# Read the input matrix
for row in range(n):
    matrix.append(input().split())

# Find Alice's initial position
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"  # Mark Alice's initial position as visited
            alice = [row, col]

# Possible move directions (up, down, left, right)
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

tea_bags = 0

# Loop until Alice has collected at least 10 tea bags
while tea_bags < 10:
    command = input()
    
    # Get the move direction based on the command
    move = possible_moves[command]
    
    # Calculate Alice's new position
    row = alice[0] + move[0]
    col = alice[1] + move[1]
    
    # Check if the new position is outside the bounds of the matrix
    if row < 0 or row >= n or col < 0 or col >= n:
        break
    
    # If Alice steps on a "R" (rock), she can't move there
    if matrix[row][col] == "R":
        continue
    
    # If Alice steps on a tea bag, collect it
    if matrix[row][col] not in "*.":
        tea_bags += int(matrix[row][col])
    
    # Mark the new position as visited
    matrix[row][col] = "*"
    
    # Update Alice's position
    alice = [row, col]

# Check if Alice has collected enough tea bags
if tea_bags >= 10:
    print("She did it! She went to the party")
else:
    print("Alice didn't make it to the tea party")

# Print the final matrix
[print(" ".join(row)) for row in matrix]
