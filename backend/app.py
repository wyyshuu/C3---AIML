from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# --- Buyer and Seller Logic ---

class OfferHistory(BaseModel):
    round: int
    buyer_offer: int
    seller_offer: int
    action: str

class NegotiationResponse(BaseModel):
    success: bool
    final_price: int | None
    history: List[OfferHistory]

@app.get("/")
def home():
    return {"message": "Negotiation API is running!"}

@app.post("/negotiate", response_model=NegotiationResponse)
def negotiate(
    buyer_min: int = 40,
    buyer_max: int = 80,
    seller_min: int = 60,
    seller_max: int = 120,
    max_rounds: int = 10
):
    buyer_offer = buyer_min
    seller_offer = seller_max
    history = []

    for round_num in range(1, max_rounds + 1):
        # record round state
        history.append(
            OfferHistory(
                round=round_num,
                buyer_offer=buyer_offer,
                seller_offer=seller_offer,
                action="negotiating"
            )
        )

        if buyer_offer >= seller_offer:
            history[-1].action = "deal"
            return NegotiationResponse(
                success=True,
                final_price=buyer_offer,
                history=history
            )

        # Update offers
        buyer_offer += 5
        seller_offer -= 5

    return NegotiationResponse(
        success=False,
        final_price=None,
        history=history
    )
