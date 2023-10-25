from pprint import pprint

coins = [1, 2, 4, 5]
max_change = 7
knap_arr = [[-1 for i in range(max_change + 1)] for _ in range(len(coins) + 1)]

def populate_dp():
    for i in range(len(coins) + 1):
        for j in range(max_change + 1):
            if i == 0 or j == 0:
                knap_arr[i][j] = 0
            else:
                pass
        print(knap_arr)

populate_dp()
pprint(knap_arr)
