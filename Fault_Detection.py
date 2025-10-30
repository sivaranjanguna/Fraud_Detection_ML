import pandas as pd
import streamlit as st
import joblib

model=joblib.load("Fraud_Detection_Model.pkl")

st.title("Fraud Detection Prediction App")

st.markdown("Plese Enter the translaction details and press the predict button")

st.divider()

translaction_type = st.selectbox("Translaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])
amount = st.number_input("Amount",min_value=0.0,value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)",min_value=0.0,value=1000.0)
newbalanceOrig = st.number_input("New Balance (Sender)",min_value=0.0,value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)",min_value=0.0,value=0.0)
newbalanceDest = st.number_input("Old Balance (Receiver)",min_value=0.0,value=0.0)

if st.button("Predict"):
    input_data = pd.dataframe([{
        "type": translaction_type,
        "amount" : amount,
        "olgbalanceOrg" : oldbalanceOrg,
        "newbalanceOrgi" : newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error("This Translaction Can be fraud")
    else:
        st.success("This Translaction looks like it is not a fraud")