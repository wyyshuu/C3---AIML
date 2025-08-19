import streamlit as st
from buyer import ConcordiaBuyerAgent
from product import Product
from negotiation import run_negotiation


st.title("🤝 Concordia Negotiation Simulator")

# User selects negotiation strategy
strategy = st.selectbox("Choose Buyer Strategy", ["standard", "bargain_hard", "quick_deal"])

# Product input
product_name = st.text_input("Enter Product Name", "Mangoes")
product = Product(name=product_name, base_market_price=100)

# Scenario setup
scenario = st.radio("Mode", ["Auto Negotiation", "Interactive Seller"])

buyer_budget = st.number_input("Buyer Budget", min_value=50, max_value=500, value=120)
seller_min = st.number_input("Seller Minimum Price", min_value=50, max_value=500, value=80)

buyer = ConcordiaBuyerAgent()
buyer.strategy = strategy  # assign strategy

if st.button("Start Negotiation"):
    if scenario == "Auto Negotiation":
        result = run_negotiation(buyer, product, buyer_budget, seller_min)
        st.subheader("📜 Conversation Log")
        for turn in result["conversation"]:
            if "buyer" in turn:
                st.markdown(f"**Buyer:** {turn['buyer']}")
            else:
                st.markdown(f"**Seller:** {turn['seller']}")
        st.subheader("📊 Results")
        st.json(result)

    elif scenario == "Interactive Seller":
        st.subheader("💬 Interactive Seller Mode")
        if "conversation" not in st.session_state:
            st.session_state.conversation = []
        if "round" not in st.session_state:
            st.session_state.round = 0

        if st.session_state.round == 0:
            opening = buyer.generate_opening_offer(product)
            st.session_state.conversation.append({"buyer": opening})
            st.session_state.round += 1

        for turn in st.session_state.conversation:
            if "buyer" in turn:
                st.markdown(f"**Buyer:** {turn['buyer']}")
            else:
                st.markdown(f"**You (Seller):** {turn['seller']}")

        seller_offer = st.text_input("Enter your counter-offer (numeric):")
        if st.button("Send Offer"):
            if seller_offer.strip():
                st.session_state.conversation.append({"seller": seller_offer})
                buyer_reply = buyer.respond_to_seller_offer(seller_offer, product)
                st.session_state.conversation.append({"buyer": buyer_reply})
                st.session_state.round += 1
