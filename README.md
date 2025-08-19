# C3 - AI Negotiation Agent

A Streamlit-based application that simulates and facilitates automated negotiation between buyers and sellers using AI agents.

## 🚀 Features

*   **Product Management:** Define products with base prices and constraints.
*   **Buyer Agent:** An AI agent that represents a buyer with a specific strategy.
*   **Negotiation Protocol:** The core logic that handles the offer/counter-offer process.
*   **Interactive UI:** A clean web interface built with Streamlit.

## 📁 Project Structure
C3---AIML/
├── buyer.py # Buyer agent logic and class
├── product.py # Product data model
├── negotiation.py # Core negotiation protocol
├── negotiation.streamlit_app.py # Main Streamlit application
├── backend/ # (Optional) Folder for additional backend code
└── README.md # This file

## 🛠️ Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/wyyshuu/C3---AIML.git
    cd C3---AIML
    ```

2.  **Install required Python packages**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file listing your dependencies, like `streamlit`)*

3.  **Run the application**
    ```bash
    streamlit run negotiation.streamlit_app.py
    ```

## 🧪 How to Use

1.  Launch the app as shown above.
2.  Define a product in the sidebar.
3.  Configure the buyer agent's parameters.
4.  Initiate the negotiation and watch the AI agents make deals!

## 👥 Contributors

- [Your Name](https://github.com/wyyshuu)
