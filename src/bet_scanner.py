import json

class BetScanner:
    def __init__(self, threshold: float, min_bet_size: float):
        self.threshold = threshold
        self.min_bet_size = min_bet_size

    def analyze_trades(self, trades):
        large_bets = []
        for trade in trades:
            if trade['amount'] >= self.min_bet_size and trade['price'] >= self.threshold:
                large_bets.append(trade)
        return large_bets

if __name__ == "__main__":
    # Example usage
    sample_trades = [
        {"amount": 1000, "price": 5.0},
        {"amount": 500, "price": 6.0},
        {"amount": 2000, "price": 4.0},
    ]
    
    scanner = BetScanner(threshold=5.0, min_bet_size=1000)
    large_bets = scanner.analyze_trades(sample_trades)
    print("Large Bets:", json.dumps(large_bets, indent=2))