import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Load Model
# ----------------------------
import sklearn
import joblib

st.write("✅ Streamlit started")
st.write("Python is working")
st.write("Scikit-learn:", sklearn.__version__)
st.write("Joblib:", joblib.__version__)

try:
    model = joblib.load("hotel_booking_model.pkl")
    st.success("✅ Model Loaded Successfully")
except Exception as e:
    st.error("❌ Model Loading Failed")
    st.exception(e)
    st.stop()
#model = joblib.load("hotel_booking_model.pkl")

# ----------------------------
# Title
# ----------------------------
st.set_page_config(
    page_title="Hotel Booking Prediction",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

/* ---------- Main Background ---------- */
.stApp{
    background: linear-gradient(135deg,#1d0b0b,#2b0f14,#3d1313);
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"]{
    background:#341417;
}

/* ---------- Headers ---------- */
h1{
    color:#FFD166;
    font-weight:700;
}

h2{
    color:#F4F4F4;
}

h3{
    color:#F4F4F4;
}

/* ---------- Input Boxes ---------- */

div[data-baseweb="select"] > div{
    background:#402126 !important;
    border-radius:12px;
}

input{
    background:#402126 !important;
    color:white !important;
}

/* ---------- Number Inputs ---------- */

[data-testid="stNumberInput"] input{
    background:#402126 !important;
    color:white !important;
}

/* ---------- Text Input ---------- */

[data-testid="stTextInput"] input{
    background:#402126 !important;
    color:white !important;
}

/* ---------- Button ---------- */

.stButton>button{

    background:linear-gradient(90deg,#8B0000,#C1121F);

    color:white;

    height:55px;

    border:none;

    border-radius:12px;

    font-size:20px;

    font-weight:bold;
}

.stButton>button:hover{

    background:linear-gradient(90deg,#C1121F,#E63946);

    transform:scale(1.02);
}

/* ---------- Success ---------- */

[data-testid="stAlert"]{

    border-radius:15px;

}

/* ---------- Metric ---------- */

[data-testid="stMetric"]{

    background:#402126;

    padding:18px;

    border-radius:15px;

}

/* ---------- Horizontal line ---------- */

hr{

    border:1px solid #5c2222;

}

/* ---------- Selectbox Label ---------- */

label{

    font-weight:bold;

    color:#F8F8F8;

}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
# 🏨 Hotel Booking Cancellation Prediction

### ✨ End-to-End Machine Learning Project
""")
st.caption("Machine Learning Project using Logistic Regression")
st.success("Model Loaded Successfully ✅")
st.markdown("### 🎮 Quick Demo")

col1, col2, col3 = st.columns(3)

demo_safe = col1.button("🟢 Safe Booking")

demo_cancel = col2.button("🔴 Cancellation")

reset = col3.button("🧹 Reset")

# ----------------------------
# Session State Defaults
# ----------------------------

default_values = {
    "hotel": "Resort Hotel",
    "lead_time": 50,
    "arrival_month": "January",
    "weekend": 1,
    "week": 2,
    "adults": 2,
    "children": 0,
    "babies": 0,
    "meal": "BB",
    "country": "PRT",
    "market": "Online TA",
    "distribution": "TA/TO",
    "reserved": "A",
    "assigned": "A",
    "deposit": "No Deposit",
    "customer": "Transient",
    "repeat": 0,
    "cancel": 0,
    "previous": 0,
    "changes": 0,
    "adr": 100.0,
    "parking": 0,
    "requests": 1
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

if demo_safe:

    st.session_state.hotel = "Resort Hotel"
    st.session_state.lead_time = 20
    st.session_state.arrival_month = "July"
    st.session_state.weekend = 2
    st.session_state.week = 3
    st.session_state.adults = 2
    st.session_state.children = 1
    st.session_state.babies = 0
    st.session_state.meal = "BB"
    st.session_state.country = "PRT"
    st.session_state.market = "Online TA"
    st.session_state.distribution = "TA/TO"
    st.session_state.reserved = "A"
    st.session_state.assigned = "A"
    st.session_state.deposit = "No Deposit"
    st.session_state.customer = "Transient"
    st.session_state.repeat = 1
    st.session_state.cancel = 0
    st.session_state.previous = 3
    st.session_state.changes = 1
    st.session_state.adr = 180.0
    st.session_state.parking = 0
    st.session_state.requests = 3

    st.rerun()
if demo_cancel:

    st.session_state.hotel = "City Hotel"
    st.session_state.lead_time = 320
    st.session_state.arrival_month = "December"
    st.session_state.weekend = 1
    st.session_state.week = 2
    st.session_state.adults = 2
    st.session_state.children = 0
    st.session_state.babies = 0
    st.session_state.meal = "SC"
    st.session_state.country = "PRT"
    st.session_state.market = "Online TA"
    st.session_state.distribution = "TA/TO"
    st.session_state.reserved = "A"
    st.session_state.assigned = "A"
    st.session_state.deposit = "No Deposit"
    st.session_state.customer = "Transient"
    st.session_state.repeat = 0
    st.session_state.cancel = 0
    st.session_state.previous = 0
    st.session_state.changes = 0
    st.session_state.adr = 60.0
    st.session_state.parking = 0
    st.session_state.requests = 2

    st.rerun()
if reset:
    for key, value in default_values.items():
        st.session_state[key] = value
    st.rerun()

st.image(
    "images/hotel_banner.jpg",
    use_container_width=True
)
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hotel.png", width=80)

    st.title("Hotel Booking")

    st.markdown("---")

    st.success("✅ Model Loaded")

    st.metric("🎯 Accuracy", "79.4%", "Best Model")
    st.metric("📊 Features", "24")

    st.metric("🤖 Algorithm", "Logistic Regression")

    st.markdown("---")
    st.caption("👨‍💻 Developed by Sameer Adnan")

    st.info(
        "Predict whether a hotel booking is likely to be cancelled."
    )
# ----------------------------
# Booking Details
# ----------------------------

st.header("📋 Booking Details")


col1, col2 = st.columns(2)

with col1:

    hotel_options = ["Resort Hotel", "City Hotel"]

    hotel = st.selectbox(
        "Hotel",
        hotel_options,
        key="hotel"
    )

    month_name = st.selectbox(
        "Arrival Month",
        list(months.keys()),
        key="arrival_month"
    )

    stays_in_weekend_nights = st.number_input(
        "Weekend Nights",
        min_value=0,
        key="weekend"
    )

with col2:

    lead_time = st.number_input(
        "Lead Time",
        min_value=0,
        key="lead_time"
    )

    stays_in_week_nights = st.number_input(
        "Week Nights",
        min_value=0,
        key="week"
    )

arrival_date_month = months[month_name]


# ----------------------------
# Guest Details
# ----------------------------

st.header("👨‍👩‍👧 Guest Details")

col1, col2, col3 = st.columns(3)

with col1:
    adults = st.number_input(
        "Adults",
        min_value=1,
        key="adults"
    )

with col2:
    children = st.number_input(
        "Children",
        min_value=0,
        key="children"
    )

with col3:
    babies = st.number_input(
        "Babies",
        min_value=0,
        key="babies"
    )
# ----------------------------
# Customer Details
# ----------------------------

st.header("🌍 Customer Details")

col1, col2 = st.columns(2)

with col1:

    meal_options = ["BB","HB","FB","SC","Undefined"]

    meal = st.selectbox(
        "Meal",
        meal_options,
        key="meal"
    )

    market_options = [
        "Online TA",
        "Offline TA/TO",
        "Direct",
        "Groups",
        "Corporate",
        "Complementary",
        "Aviation"
    ]

    market_segment = st.selectbox(
        "Market Segment",
        market_options,
        key="market"
    )

with col2:

    country = st.text_input(
        "Country",
        key="country"
    )

    distribution_options = [
    "TA/TO",
    "Direct",
    "Corporate",
    "GDS"
    ]

    distribution_channel = st.selectbox(
        "Distribution Channel",
        distribution_options,
        key="distribution"
    )
# ----------------------------
# Room Details
# ----------------------------

st.header("🛏 Room Details")

col1, col2 = st.columns(2)

with col1:

    room_options = ["A","B","C","D","E","F","G","H","L","P"]

    reserved_room_type = st.selectbox(
        "Reserved Room",
        room_options,
        key="reserved"
    )

    deposit_options = [
    "No Deposit",
    "Refundable",
    "Non Refund"
    ]

    deposit_type = st.selectbox(
        "Deposit",
        deposit_options,
        key="Deposit"
    )

with col2:

    assigned_room_type = st.selectbox(
        "Assigned Room",
        room_options,
        key="assigned"
    )

    customer_options = [
    "Transient",
    "Transient-Party",
    "Contract",
    "Group"
    ]

    customer_type = st.selectbox(
        "Customer Type",
        customer_options,
        key="customer"
    )
# ----------------------------
# Booking History
# ----------------------------

st.header("📈 Booking History")

col1, col2 = st.columns(2)

with col1:

    is_repeated_guest = st.selectbox(
    "Repeated Guest",
    [0,1],
    key="repeat"
    )

    previous_cancellations = st.number_input(
    "Previous Cancellations",
    min_value=0,
    key="cancel"
    )

with col2:

    previous_bookings_not_canceled = st.number_input(
    "Previous Bookings",
    min_value=0,
    key="previous"
    )

    booking_changes = st.number_input(
    "Booking Changes",
    min_value=0,
    key="changes"
    )

# ----------------------------
# Pricing & Other Details
# ----------------------------

st.header("💰 Price Details")

col1, col2 = st.columns(2)

with col1:

    adr = st.number_input(
    "ADR",
    min_value=0.0,
    key="adr"
    )

    required_car_parking_spaces = st.number_input(
    "Parking Spaces",
    min_value=0,
    key="parking"
    )
# Calculate first
total_stay = stays_in_weekend_nights + stays_in_week_nights

with col2:

    total_of_special_requests = st.number_input(
    "Special Requests",
    min_value=0,
    key="requests"
    )

    st.metric(
        "Total Stay",
        total_stay
    )
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏨 Hotel", hotel)

with col2:
    st.metric("🌙 Stay", f"{total_stay} Nights")

with col3:
    st.metric("💰 ADR", f"{adr:.2f}")
# ----------------------------
# Prediction
# ----------------------------

st.markdown("---")

predict = st.button(
    "🔮 Predict Booking Cancellation",
    use_container_width=True
)

if predict:

    input_df = pd.DataFrame({
        "hotel": [hotel],
        "lead_time": [lead_time],
        "arrival_date_month": [arrival_date_month],
        "stays_in_weekend_nights": [stays_in_weekend_nights],
        "stays_in_week_nights": [stays_in_week_nights],
        "adults": [adults],
        "children": [children],
        "babies": [babies],
        "meal": [meal],
        "country": [country],
        "market_segment": [market_segment],
        "distribution_channel": [distribution_channel],
        "is_repeated_guest": [is_repeated_guest],
        "previous_cancellations": [previous_cancellations],
        "previous_bookings_not_canceled": [previous_bookings_not_canceled],
        "reserved_room_type": [reserved_room_type],
        "assigned_room_type": [assigned_room_type],
        "booking_changes": [booking_changes],
        "deposit_type": [deposit_type],
        "customer_type": [customer_type],
        "adr": [adr],
        "required_car_parking_spaces": [required_car_parking_spaces],
        "total_of_special_requests": [total_of_special_requests],
        "total_stay": [total_stay]
    })

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)
    confidence = probability.max() * 100

    st.markdown("## 🎯 Prediction Result")

    cancel_prob = probability[0][1] * 100
    confirm_prob = probability[0][0] * 100

    col1, col2, col3 = st.columns(3)

    with col1:

        if prediction[0] == 1:

            st.error("❌ Booking Likely to be Cancelled")

        else:

            st.success("✅ Booking Likely to be Confirmed")

    with col2:

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    with col3:

        if prediction[0] == 1:

            st.metric(
                "Cancellation Probability",
                f"{cancel_prob:.2f}%"
            )

        else:

            st.metric(
                "Confirmation Probability",
                f"{confirm_prob:.2f}%"
            )

    st.progress(confidence/100)
    st.markdown("---")

    st.markdown(
    """
    <div style="text-align:center">

    Made with ❤️ using <b>Streamlit</b> & <b>Scikit-Learn</b>

    <br><br>

    🏨 Hotel Booking Cancellation Prediction

    <br>

    © 2026 Sameer Adnan

    </div>
    """,
    unsafe_allow_html=True
    )
with st.expander("ℹ About This Project"):

    st.write(
        """
        This project predicts hotel booking cancellations using
        Logistic Regression trained on historical booking data.
        """
    )