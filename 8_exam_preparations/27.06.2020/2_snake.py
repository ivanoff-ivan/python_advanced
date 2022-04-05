n = int(input())
matrix = []
snake_row_coordinate = 0
snake_col_coordinate = 0
for i in range(n):
    line = [x for x in input()]
    matrix.append(line)
    if "S" in line:
        snake_row_coordinate = i
        snake_col_coordinate = line.index("S")

food_quantity = 0
directions = {"up": (-1,0), "right":(0,1), "down":(1, 0), "left":(0,-1)}
game_over = False

while True:
    if food_quantity >= 10:
        break

    direction = input()
    if direction in directions.keys():
        row_changes = directions[direction][0]
        col_changes = directions[direction][1]

        if 0 <= snake_row_coordinate + row_changes < n and 0 <= snake_col_coordinate + col_changes < n:
            matrix[snake_row_coordinate][snake_col_coordinate] = "."
            snake_row_coordinate += row_changes
            snake_col_coordinate += col_changes
            if matrix[snake_row_coordinate][snake_col_coordinate] == "*":
                food_quantity += 1
            elif matrix[snake_row_coordinate][snake_col_coordinate] == "B":
                matrix[snake_row_coordinate][snake_col_coordinate] = "."
                for i in range(n):
                    for j in range(n):
                        if matrix[i][j] =="B":
                            if i != snake_row_coordinate or j != snake_col_coordinate:
                                snake_row_coordinate = i
                                snake_col_coordinate = j

            matrix[snake_row_coordinate][snake_col_coordinate] = "S"
        else:
            matrix[snake_row_coordinate][snake_col_coordinate] = "."
            game_over = True
            break

if not game_over:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_quantity}")
for i in range(n):
    print("".join(matrix[i]))