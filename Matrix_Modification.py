n = int(input())

matrix = [[int(i) for i in input().split()]for _ in range(n)]

while True:
    line = input().split()
    if line[0] == "END":
        break
    command = line[0]

    row,col,valu = map(int, line[1:])

    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid cordinates")
        continue
    
    if command == "ADD":
        matrix[row][col] += valu
    elif command == "Subtract":
        matrix[row][col] -= valu
    

[print(*row) for row in matrix] 
