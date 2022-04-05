tokens = input().split()
main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

formed_colors = []
while tokens:
    first_token = tokens.pop(0)
    if tokens:
        last_token = tokens.pop()
    else:
        last_token = ""

    if first_token + last_token in main_colors:
        formed_colors.append(first_token + last_token)
        main_colors.remove(first_token + last_token)
    elif last_token + first_token in main_colors:
        formed_colors.append((last_token + first_token))
        main_colors.remove(last_token + first_token)
    elif first_token + last_token in secondary_colors:
        formed_colors.append(first_token + last_token)
    elif last_token + first_token in secondary_colors:
        formed_colors.append(last_token + first_token)
    else:
        first_token = first_token[:-1]
        last_token = last_token[:-1]
        if first_token:
            tokens.insert(len(tokens) // 2, first_token)
        if last_token:
            tokens.insert(len(tokens) // 2, last_token)

for color in formed_colors:
    if color in secondary_colors.keys():
        if any(x not in formed_colors for x in secondary_colors[color]):
            formed_colors.remove(color)

print(formed_colors)
