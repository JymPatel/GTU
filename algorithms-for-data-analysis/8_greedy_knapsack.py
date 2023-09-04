p = [10, 5, 15, 7, 6, 18, 3]
w = [2, 3, 5, 7, 1, 4, 1]

max_weight = 15

rel_weights = [p[i] / w[i] for i in range(len(p))]
weights = []

for i in range(len(p)):
    weights.append([p[i], w[i], rel_weights[i]])
weights.sort(key=lambda x: x[2])
weights.reverse()
print(weights)

proportions = [0 for _ in range(len(p))]
i = 0
possible = 0
while max_weight > 0:
    if weights[i][1] <= max_weight:
        max_weight -= weights[i][1]
        possible += weights[i][0]
        proportions[i] = 1
    else:
        possible += weights[i][2] * max_weight
        proportions[i] = max_weight / weights[i][1]
        max_weight = 0
    i += 1

print(f"Max returns: {possible}")

for i in range(len(p)):
    print(f"({weights[i][0]}, {weights[i][1]}) has proportion {proportions[i]}")
