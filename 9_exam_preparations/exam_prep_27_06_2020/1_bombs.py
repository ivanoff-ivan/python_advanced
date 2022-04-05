from collections import deque


bombs = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}

pouch = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

bomb_effects = deque(input().split(", "))
bomb_casings = input().split(", ")
success = False

while True:
    if not bomb_effects or not bomb_casings:
        break
    if pouch["Datura Bombs"] >= 3 and pouch["Cherry Bombs"] >= 3 and pouch["Smoke Decoy Bombs"] >= 3:
        success = True
        break
    first_effect = int(bomb_effects.popleft())
    last_casing = int(bomb_casings.pop())
    result = first_effect + last_casing
    matched = False
    for key,value in bombs.items():
        if result == value:
            pouch[key] += 1
            matched = True
            break

    if not matched:
        last_casing -= 5
        bomb_effects.appendleft(first_effect)
        bomb_casings.append(last_casing)

if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(bomb_casings)}")
else:
    print("Bomb Casings: empty")

pouch = dict(sorted(pouch.items(), key=lambda x: x[0])) # ako ima greshka tuka e
for k,v in pouch.items():
    print(f"{k}: {v}")