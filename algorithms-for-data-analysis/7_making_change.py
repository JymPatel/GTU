coins = [1, 2, 5, 10, 20]
max_change = 40
knap_arr = [[-1 for i in range(max_change + 1)] for _ in range(len(coins) + 1)]

def make_coin(change, coin_no):
    coin_no -= 1
    if change <= 0 or coin_no <= 0:
        return (0, [])
    
    if change < w[coin_no]:
        knap_arr[coin_no][change] = make_coin(change, coin_no)
        return knap_arr[coin_no][change]
    p1 = p[coin_no] + make_coin(change - w[coin_no], coin_no)[0]
    p2, p2_arr = make_coin(change, coin_no)
    if p2 >= p1:
        knap_arr[coin_no][change] = [p2, p2_arr]
    else:
        knap_arr[coin_no][change] = [p1, make_coin(change - w[coin_no], coin_no)[1] + [w[coin_no]]]
    return knap_arr[coin_no][change]