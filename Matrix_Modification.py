n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

while True:
    line = input().split()
    if line[0] == "END":
        break
    command = line[0].upper()  # Make the command case-insensitive by converting it to uppercase

    row, col, value = map(int, line[1:])

    # Check for invalid coordinates
    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid coordinates")
        continue

    if command == "ADD":
        matrix[row][col] += value
    elif command == "SUBTRACT":
        matrix[row][col] -= value
    else:
        print("Invalid command")
        continue

# Print the final matrix
for row in matrix:
    print(*row)
