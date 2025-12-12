import pandas as pd
import streamlit as st
import joblib

# Load the trained model
model = joblib.load("Fraud_Detection_Model.pkl")

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="⚠️",
    layout="wide"
)

# -----------------------------------
# Premium CSS (Gradient + Neumorphic + Glow Buttons)
# -----------------------------------
st.markdown("""
    <style>
        .stApp { background: linear-gradient(145deg, #0a0a0a, #1a1a1a); }
        .navbar { width: 100%; padding: 15px 25px; background: rgba(255, 140, 0, 0.15); border-bottom: 2px solid #FFA500; backdrop-filter: blur(6px); border-radius: 0 0 12px 12px; }
        .navbar h2 { color: #FFA500; text-shadow: 0px 0px 12px #ff8c00; font-weight: 900; margin: 0; text-align: center; }
        .title-text { margin-top: 10px; font-size: 42px; color: #FFA500; font-weight: 900; text-align: center; text-shadow: 0px 0px 12px #ff8c00; }
        .subtitle-text { text-align: center; color: #ccc; font-size: 18px; margin-bottom: 25px; }
        .neumorphic-box { background: #121212; padding: 30px; border-radius: 20px; box-shadow: 10px 10px 20px #0a0a0a, -10px -10px 20px #1e1e1e; border: 1px solid #222; }
        .stSelectbox label, .stNumberInput label { color: #FFA500 !important; font-size: 17px; font-weight: 600; }
        .stButton button { background: #FFA500; color: black; border: none; border-radius: 12px; padding: 12px 25px; font-size: 20px; font-weight: 700; box-shadow: 0px 0px 16px #ff8c00; transition: 0.3s; width: 250px; }
        .stButton button:hover { background: #ffb74d; box-shadow: 0px 0px 25px #ffa640; transform: scale(1.05); }
        @keyframes popin { from { transform: scale(0.7); opacity: 0; } to { transform: scale(1); opacity: 1; } }
        .prediction-card { background: #1a1a1a; padding: 25px; border-left: 5px solid #FFA500; border-radius: 12px; animation: popin 0.4s ease-out; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------
# Navigation Bar
# -----------------------------------
st.markdown("<div class='navbar'><h2>⚠️ Fraud Detection System</h2></div>", unsafe_allow_html=True)

# Title + Subtitle
st.markdown("<div class='title-text'>Intelligent Fraud Detection Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>Enter transaction details below to predict fraud</div>", unsafe_allow_html=True)

st.divider()

# -----------------------------------
# Input Section (3-row layout)
# -----------------------------------
cols = st.columns([1, 2, 1])
col_center = cols[1]

with col_center:
    st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)

    # Row 1: Transaction Type | Amount
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        transaction_type = st.selectbox(
            "Transaction Type",
            ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
        )
    with r1c2:
        amount = st.number_input("Amount", min_value=0.0, value=1000.0)

    # Row 2: Sender New Balance | Sender Old Balance
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
    with r2c2:
        oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)

    # Row 3: Receiver New Balance | Receiver Old Balance
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)
    with r3c2:
        oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------
# Predict Button (Centered)
# -----------------------------------
btn_cols = st.columns([1, 1, 1])
btn_center = btn_cols[1]

with btn_center:
    predict_clicked = st.button("🚀 Predict")

# -----------------------------------
# Prediction Result
# -----------------------------------
if predict_clicked:
    # Ensure column names match the model's training
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    result_cols = st.columns([1, 2, 1])
    result_box = result_cols[1]

    with result_box:
        st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)

        st.subheader(f"🔍 Prediction Result: **{int(prediction)}**")

        if prediction == 1:
            st.error("⚠️ **This Transaction is Likely Fraudulent!**")
        else:
            st.success("✔️ **This Transaction Appears Safe.**")

        st.markdown("</div>", unsafe_allow_html=True)
