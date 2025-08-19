from typing import Dict, Any, List, Optional
from buyer import ConcordiaBuyerAgent
from product import Product


def run_negotiation(
    buyer: ConcordiaBuyerAgent,
    product: Product,
    buyer_budget: int,
    seller_min: int,
    max_rounds: int = 10,
) -> Dict[str, Any]:
    conversation: List[Dict[str, str]] = []
    deal_made = False
    final_price: Optional[int] = None

    # Buyer makes opening offer
    buyer_message = buyer.generate_opening_offer(product)
    conversation.append({"buyer": buyer_message})

    current_price = product.base_market_price

    for round_num in range(1, max_rounds + 1):
        # Simulate seller counter
        if current_price > seller_min:
            current_price -= 5
        seller_offer = str(current_price)
        conversation.append({"seller": seller_offer})

        # Buyer responds
        buyer_message = buyer.respond_to_seller_offer(seller_offer, product)
        conversation.append({"buyer": buyer_message})

        if "Deal" in buyer_message:
            deal_made = True
            final_price = int(seller_offer)
            break

    savings_vs_budget = buyer_budget - (final_price or buyer_budget)
    savings_pct_of_budget = (
        (savings_vs_budget / buyer_budget) * 100 if buyer_budget else 0
    )
    below_market_pct = (
        ((product.base_market_price - (final_price or product.base_market_price))
         / product.base_market_price) * 100
    )

    return {
        "deal_made": deal_made,
        "final_price": final_price,
        "rounds": round_num,
        "savings_vs_budget": savings_vs_budget,
        "savings_pct_of_budget": savings_pct_of_budget,
        "below_market_pct": below_market_pct,
        "conversation": conversation,
        "buyer_memory": buyer.memory,
    }
