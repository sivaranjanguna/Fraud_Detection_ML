# -----------------------------------
# INPUT SECTION (Centered Neumorphic Card)
# -----------------------------------
colC = st.columns([1, 2, 1])[1]  # Center column

with colC:
    st.markdown("<div class='neumorphic-box'>", unsafe_allow_html=True)

    # Row 1 ──────────────────────────────────
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        translaction_type = st.selectbox(
            "Transaction Type",
            ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
        )
    with r1c2:
        amount = st.number_input("Amount", min_value=0.0, value=1000.0)

    # Row 2 ──────────────────────────────────
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        newbalanceOrig = st.number_input(
            "New Balance (Sender)",
            min_value=0.0,
            value=9000.0
        )
    with r2c2:
        oldbalanceOrg = st.number_input(
            "Old Balance (Sender)",
            min_value=0.0,
            value=1000.0
        )

    # Row 3 ──────────────────────────────────
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        newbalanceDest = st.number_input(
            "New Balance (Receiver)",
            min_value=0.0,
            value=0.0
        )
    with r3c2:
        oldbalanceDest = st.number_input(
            "Old Balance (Receiver)",
            min_value=0.0,
            value=0.0
        )

    st.markdown("</div>", unsafe_allow_html=True)
