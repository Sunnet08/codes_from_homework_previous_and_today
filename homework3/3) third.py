from typing import List

def max_profit(prices: List[int]):
    # если мало данных, профита нет
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    best = 0

    for p in prices:
        # возможный профит если продать сейчас
        prof = p - min_price
        if prof > best:
            best = prof
        # обновляем минимальную цену
        if p < min_price:
            min_price = p

    return best

# print(max_profit([7,1,5,3,6,4]))
