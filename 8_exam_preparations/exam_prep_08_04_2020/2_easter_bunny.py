import sys


def is_valid(number, size):
    return 0 <= number < size


n = int(input())
directions = {"up": (-1,0), "right":(0,1), "down":(1, 0), "left":(0,-1)}
bunny_coordinates = ()
best_sum = -sys.maxsize
best_direction = ""
best_coordinates = []
matrix = []
for i in range(n):
    row = input().split()
    matrix.append(row)
    if "B" in row:
        bunny_col = row.index("B")
        bunny_row = i
        bunny_coordinates = (bunny_row, bunny_col)

for direction in directions:
    current_sum = 0
    current_coordinates = []
    row = bunny_coordinates[0]
    col = bunny_coordinates[1]
    row_changes = directions[direction][0]
    col_changes = directions[direction][1]
    if not is_valid(row + row_changes, n) or not is_valid(col+col_changes, n):
        continue

    while is_valid(row, n) and is_valid(col, n):
        current_cell = matrix[row][col]
        if current_cell != "B" and current_cell != "X":
            current_sum += int(current_cell)
            current_coordinates.append([row, col])
        elif current_cell == "X":
            break
        row += row_changes
        col += col_changes
    
    if current_sum > best_sum:
        best_sum = current_sum
        best_direction = direction
        best_coordinates = current_coordinates

print(best_direction)
[print(x) for x in best_coordinates]
print(best_sum)
