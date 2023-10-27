from pprint import pprint

p = [10, 5, 15, 7, 6, 18, 3]
w = [2, 3, 5, 7, 1, 4, 1]

max_weight = 15
knap_arr = [[-1 for i in range(max_weight + 1)] for _ in range(len(w))]

def knapsack01(weight = max_weight, obj_no=len(w)):
    obj_no -= 1
    if weight <= 0 or obj_no <= 0:
        return (0, [])
    
    if weight < w[obj_no]:
        knap_arr[obj_no][weight] = knapsack01(weight, obj_no)
        return knap_arr[obj_no][weight]
    p1 = p[obj_no] + knapsack01(weight - w[obj_no], obj_no)[0]
    p2, p2_arr = knapsack01(weight, obj_no)
    if p2 >= p1:
        knap_arr[obj_no][weight] = [p2, p2_arr]
    else:
        knap_arr[obj_no][weight] = [p1, knapsack01(weight - w[obj_no], obj_no)[1] + [w[obj_no]]]
    return knap_arr[obj_no][weight]

profit, objects = knapsack01()
print(f"max profit of {profit} can be made using {objects}")
for i in range(len(knap_arr[0])):
    knapsack01(i)
print(knap_arr)

knap_arr2 = [[-1 for i in range(max_weight + 1)] for _ in range(len(w))]
for i in range(len(knap_arr)):
    for j in range(len(knap_arr[i])):
        if knap_arr[i][j] == -1:
            knap_arr2[i][j] = -1
        else:
            knap_arr2[i][j] = knap_arr[i][j][0]

pprint(knap_arr2)
