import requests
import websocket
import json

class PolymarketAPI:
    BASE_URL = 'https://api.polymarket.com/v1/'

    def __init__(self):
        self.ws = None

    def fetch_markets(self):
        response = requests.get(f'{self.BASE_URL}markets')
        return response.json()

    def fetch_trades(self, market_id):
        response = requests.get(f'{self.BASE_URL}markets/{market_id}/trades')
        return response.json()

    def fetch_real_time_data(self, market_id):
        self.ws = websocket.create_connection(f'wss://api.polymarket.com/v1/markets/{market_id}/updates')
        while True:
            try:
                result = self.ws.recv()
                print(json.loads(result))
            except websocket.WebSocketConnectionClosedException:
                break

    def close_connection(self):
        if self.ws:
            self.ws.close()