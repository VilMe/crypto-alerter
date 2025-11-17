import requests
from dataclasses import dataclass
from typing import Final


BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'

@dataclass
class Coin: 
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float


    def __str__(self):
        return f'{self.name} ({self.symbold}): ${self.current_price:,}'
    

def get_coint() -> list[Coin]:
    payload:dit = {'vs_currency': 'usd', 'order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    json: dict = data.json()

    