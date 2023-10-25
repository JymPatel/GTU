from pprint import pprint

coins = [1, 2, 4, 5]
max_change = 8
knap_arr = [[0 for i in range(max_change + 1)] for _ in range(len(coins) + 1)]

def populate_dp():
    for i in range(max_change + 1):
        knap_arr[0][i] = 0
    for i in range(1, len(coins) + 1):
        for j in range(coins[i - 1]):
            knap_arr[i][j] = knap_arr[i - 1][j]
        for j in range(coins[i - 1], max_change + 1):
            knap_arr[i][j] = 1 + knap_arr[i][j - coins[i - 1]]

def get_change(change, max_coin = len(coins)):
    print(f"({change}, {coins[max_coin - 1]})")
    if change <= 0:
        return []
    if knap_arr[max_coin][change] == knap_arr[max_coin - 1][change]:
        return get_change(change, max_coin - 1)
    else:
        c = get_change(change - coins[max_coin - 1], max_coin)
        c.append(coins[max_coin - 1])
        return c


populate_dp()
pprint(knap_arr)
pprint(get_change(8))
