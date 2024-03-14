BACKPACK_HEIGHT = 4
BACKPACK_WIDHT = 2

backpack_size = BACKPACK_HEIGHT * BACKPACK_WIDHT
items = {
    'r': {'size': 3, 'points': 25},
    'p': {'size': 2, 'points': 15},
    'a': {'size': 2, 'points': 15},
    'm': {'size': 2, 'points': 20},
    'i': {'size': 1, 'points': 5},
    'k': {'size': 1, 'points': 15},
    'x': {'size': 3, 'points': 20},
    't': {'size': 1, 'points': 25},
    'f': {'size': 1, 'points': 15},
    'd': {'size': 1, 'points': 10},
    's': {'size': 2, 'points': 20},
    'c': {'size': 2, 'points': 20},
}

initial_points = -sum(item['points'] for item in items.values())
dp = [[initial_points for _ in range(backpack_size + 1)]]
dp[0][0] = 0

for i, (item, attrs) in enumerate(items.items(), start=1):
    dp.append(dp[i-1].copy())
    for j in range(attrs['size'], backpack_size + 1):
        dp[i][j] = max(dp[i][j], dp[i-1][j-attrs['size']] + 2*attrs['points'] - attrs['points'])

max_points = max(dp[-1])

chosen_items = []
size = backpack_size
for i in range(len(items), 0, -1):
    if dp[i][size] != dp[i-1][size]:
        item = list(items.keys())[i-1]
        chosen_items.append(item)
        size -= items[item]['size']

final_points = sum(items[item]['points'] for item in chosen_items) - sum(items[item]['points'] for item in items if item not in chosen_items)

inventory = [['' for _ in range(BACKPACK_HEIGHT)] for _ in range(BACKPACK_WIDHT)]
index = 0
for item in chosen_items:
    size = items[item]['size']
    for _ in range(size):
        inventory[index // 4][index % 4] = item
        index += 1

for row in inventory:
    print(row)
print(final_points)