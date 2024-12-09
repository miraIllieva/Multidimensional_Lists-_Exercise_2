n = int(input())

matrix = []

knights = []

# Read the matrix and track the positions of knights
for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == "K":
            knights.append([row, col])

remove_knights = 0
possible_moves = ((1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1))

# Loop to remove knights until no more knights can be removed
while True:
    max_hits = 0
    max_knight = None

    # For each knight, check how many other knights it can "hit" based on possible moves
    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            next_row = k_row + move[0]
            next_col = k_col + move[1]

            if 0 <= next_row < n and 0 <= next_col < n:
                if matrix[next_row][next_col] == "K":
                    hits += 1

        # Track the knight with the maximum hits
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    # If no knight can hit any other knight, stop
    if max_hits == 0:
        break

    # Remove the knight with the maximum hits
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    remove_knights += 1

# Print the total number of knights removed
print(remove_knights)
