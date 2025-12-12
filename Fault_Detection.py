import pandas as pd
import streamlit as st
import joblib

# Load Model
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
        /* Page background gradient */
        .stApp {
            background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
        }

        /* Top Navigation Bar */
        .navbar {
            width: 100%;
            padding: 15px 25px;
            background: rgba(255, 140, 0, 0.15);
            border-bottom: 2px solid #FFA500;
            backdrop-filter: blur(6px);
            border-radius: 0 0 12px 12px;
        }
        .navbar h2 {
            color: #FFA500;
            text-shadow: 0px 0px 12px #ff8c00;
            font-weight: 900;
            margin: 0;
            text-align: center;
        }

        /* Page Title */
        .title-text {
            margin-top: 10px;
            font-size: 42px;
            color: #FFA500;
            font-weight: 900;
            text-align: center;
            text-shadow: 0px 0px 12px #ff8c00;
        }

        /* Subtitle */
        .subtitle-text {
            text-align: center;
            color: #ccc;
            font-size: 18px;
            margin-bottom: 25px;
        }

        /* Neumorphic Card Styling */
        .neumorphic-box {
            background: #121212;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 10px 10px 20px #0a0a0a, 
                        -10px -10px 20px #1e1e1e;
            border: 1px solid #222;
        }

        /* Labels */
        .stSelectbox label, .stNumberInput label {
            color: #FFA500 !important;
            font-size: 17px;
            font-weight: 600;
        }

        /* Glow Button */
        .stButton button {
            background: #FFA500;
            color: black;
            border: none;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 20px;
            font-weight: 700;
            box-shadow: 0px 0px 16px #ff8c00;
            transition: 0.3s;
            width: 250px;
        }
        .stButton button:hover {
            background: #ffb74d;
            box-shadow: 0px 0px 25px #ffa640;
            transform: scale(1.05);
        }

        /* Animated Prediction Card */
        @keyframes popin {
            from { transform: scale(0.7); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        .prediction-card {
            background: #1a1a1a;
            padding: 25px;
            border-left: 5px solid #FFA500;
            border-radius: 12px;
            animation: popin 0.4s ease-out;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------
# NAVIGATION BAR
# -----------------------------------
st.markdown("<div class='navbar'><h2>⚠️ Fraud Detection System</h2></div>", unsafe_allow_html=True)

# -----------------------------------
# Title + Subtitle
# -----------------------------------
st.markdown("<div class='title-text'>Intelligent Fraud Detection Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>Enter transaction details below to predict fraud</div>", unsafe_allow_html=True)

st.divider()


# -----------------------------------
# INPUT SECTION (Centered Neumorphic Card)
# -----------------------------------
colC = st.columns([1, 2, 1])[1]  # Center column

with colC:
    st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        translaction_type = st.selectbox("Transaction Type", 
                                         ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
        amount = st.number_input("Amount", min_value=0.0, value=1000.0)
        oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)

    with c2:
        newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
        oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
        newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------
# Predict Button (Centered)
# -----------------------------------
st.write("")
btn_center = st.columns([1, 1, 1])[1]

with btn_center:
    predict_clicked = st.button("🚀 Predict")


# -----------------------------------
# PREDICTION RESULT
# -----------------------------------
if predict_clicked:
    input_data = pd.DataFrame([{
        "type": translaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    result_box = st.columns([1, 2, 1])[1]

    with result_box:
        st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)

        st.subheader(f"🔍 Prediction Result: **{int(prediction)}**")

        if prediction == 1:
            st.error("⚠️ **This Transaction is Likely Fraudulent!**")
        else:
            st.success("✔️ **This Transaction Appears Safe.**")

        st.markdown("</div>", unsafe_allow_html=True)
