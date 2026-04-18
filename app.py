import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Heart Disease App", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1 {
    text-align: center;
    color: #ff4b4b;
}
.stButton>button {
    width: 100%;
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("❤️ Heart Disease Prediction")
st.markdown("### Enter patient information")

# Layout in columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 20, 100, 50)
    trestbps = st.number_input("Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 400, 200)
    thalach = st.number_input("Max Heart Rate", 60, 220, 150)

with col2:
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain", ["typical angina", "atypical angina", "non-anginal", "asymptomatic"])

# Additional section
st.markdown("---")
st.subheader("Additional Information")

col3, col4 = st.columns(2)

with col3:
    fbs = st.selectbox("Fasting Blood Sugar > 120", [True, False])
    exang = st.selectbox("Exercise Angina", [True, False])

with col4:
    slope = st.selectbox("Slope", ["upsloping", "flat", "downsloping"])
    thal = st.selectbox("Thal", ["normal", "fixed defect", "reversable defect"])

# Convert inputs (same encoding logic as training!)
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs else 0
exang = 1 if exang else 0

# Example encoding (adapt if needed)
cp_map = {"typical angina":0, "atypical angina":1, "non-anginal":2, "asymptomatic":3}
cp = cp_map[cp]

slope_map = {"upsloping":0, "flat":1, "downsloping":2}
slope = slope_map[slope]

thal_map = {"normal":0, "fixed defect":1, "reversable defect":2}
thal = thal_map[thal]

# Prediction button
if st.button("🔍 Predict"):
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, thalach, exang, oldpeak, slope, thal]],
                              columns=['age','sex','cp','trestbps','chol','fbs','thalch','exang','oldpeak','slope','thal'])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High risk of Heart Disease")
    else:
        st.success("✅ Low risk of Heart Disease")
