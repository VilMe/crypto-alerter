from crypto_data import get_coins, Coin



def alert(symbol: str, bottom: float, top: float, coin_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!VLERT TRIGGERED !!')
            else:
                print(coin)