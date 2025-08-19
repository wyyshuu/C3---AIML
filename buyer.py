from typing import Dict, Any


class ConcordiaBuyerAgent:
    """
    A simple buyer agent that negotiates with different strategies:
    - standard: balanced negotiation
    - bargain_hard: pushes for lowest possible price
    - quick_deal: accepts reasonable offers quickly
    """

    def __init__(self):
        self.strategy = "standard"
        self.memory: Dict[str, Any] = {}

    def generate_opening_offer(self, product) -> str:
        base_price = product.base_market_price
        if self.strategy == "bargain_hard":
            offer = int(base_price * 0.6)
        elif self.strategy == "quick_deal":
            offer = int(base_price * 0.9)
        else:
            offer = int(base_price * 0.8)

        self.memory["opening_offer"] = offer
        return f"I can offer {offer} for your {product.name}."

    def respond_to_seller_offer(self, seller_offer: str, product) -> str:
        base_price = product.base_market_price

        try:
            seller_price = int(seller_offer)
        except ValueError:
            return "I didn't understand your offer. Can you give me a number?"

        if self.strategy == "bargain_hard":
            counter = max(seller_price - 5, int(base_price * 0.6))
        elif self.strategy == "quick_deal":
            if seller_price <= int(base_price * 0.9):
                return f"Deal at {seller_price}!"
            counter = int((seller_price + base_price * 0.8) / 2)
        else:  # standard
            if seller_price <= int(base_price * 0.85):
                return f"Deal at {seller_price}!"
            counter = int((seller_price + base_price * 0.75) / 2)

        self.memory["last_counter"] = counter
        return f"How about {counter}?"
