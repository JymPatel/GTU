p = [10, 5, 15, 7, 6, 18, 3]
w = [2, 3, 5, 7, 1, 4, 1]

p = [1, 6, 18, 22, 28]
w = [1, 2, 5, 6, 7]

max_weight = 11

knap_arr = [[-1 for _ in range(max_weight + 1)] for _ in range(len(w) + 1)]

def knapsack01(weight, obj_no = len(w)):
    if knap_arr[obj_no][weight] != -1:
        return knap_arr[obj_no][weight]
    if obj_no == 0 or weight == 0:
        knap_arr[obj_no][weight] = 0
        return 0
    elif obj_no < 0 or weight < 0:
        return 0
    if weight < w[obj_no - 1]:
        knap_arr[obj_no][weight] = knap_arr[obj_no - 1][weight]
    profit = p[obj_no - 1] + knap_arr[obj_no - 1][weight - w[obj_no - 1]]
    knap_arr[obj_no][weight] = max(knapsack01(weight, obj_no - 1), profit)
    return knap_arr[obj_no][weight]

knapsack01(max_weight)
print(knap_arr)
