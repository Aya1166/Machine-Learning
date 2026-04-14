import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.set_page_config(page_title="Heart Disease App", layout="centered")

st.title("❤️ Heart Disease Prediction")
st.write("Fill in the patient information below:")

# =========================
# MAIN INPUTS
# =========================

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 50)
    trestbps = st.number_input("Blood Pressure", value=120)
    chol = st.number_input("Cholesterol", value=200)
    thalach = st.number_input("Max Heart Rate", value=150)

with col2:
    oldpeak = st.number_input("Oldpeak", value=1.0)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain", [
        "typical angina",
        "atypical angina",
        "non-anginal",
        "asymptomatic"
    ])

# =========================
# ADDITIONAL INPUTS
# =========================

st.subheader("Additional Information")

col3, col4 = st.columns(2)

with col3:
    fbs = st.selectbox("Fasting Blood Sugar > 120", [True, False])
    restecg = st.selectbox("Rest ECG", ["normal", "lv hypertrophy"])

with col4:
    exang = st.selectbox("Exercise Angina", [True, False])
    slope = st.selectbox("Slope", ["upsloping", "flat", "downsloping"])
    thal = st.selectbox("Thal", ["normal", "fixed defect", "reversable defect"])

# =========================
# PREDICTION
# =========================

st.markdown("---")

if st.button("🔍 Predict"):

    # Create dataframe with EXACT training columns
    input_data = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

    # =========================
    # SAFE FEATURE FILLING
    # =========================

    # Numerical
    if 'age' in input_data.columns:
        input_data['age'] = age

    if 'trestbps' in input_data.columns:
        input_data['trestbps'] = trestbps

    if 'chol' in input_data.columns:
        input_data['chol'] = chol

    if 'thalch' in input_data.columns:
        input_data['thalch'] = thalach

    if 'oldpeak' in input_data.columns:
        input_data['oldpeak'] = oldpeak

    # Binary
    if 'sex_Male' in input_data.columns and sex == "Male":
        input_data['sex_Male'] = 1

    if 'fbs_True' in input_data.columns and fbs:
        input_data['fbs_True'] = 1

    if 'exang_True' in input_data.columns and exang:
        input_data['exang_True'] = 1

    # Chest pain
    if cp == "typical angina" and 'cp_typical angina' in input_data.columns:
        input_data['cp_typical angina'] = 1
    elif cp == "atypical angina" and 'cp_atypical angina' in input_data.columns:
        input_data['cp_atypical angina'] = 1
    elif cp == "non-anginal" and 'cp_non-anginal' in input_data.columns:
        input_data['cp_non-anginal'] = 1

    # Restecg
    if restecg == "lv hypertrophy" and 'restecg_lv hypertrophy' in input_data.columns:
        input_data['restecg_lv hypertrophy'] = 1

    # Slope
    if slope == "flat" and 'slope_flat' in input_data.columns:
        input_data['slope_flat'] = 1
    elif slope == "downsloping" and 'slope_downsloping' in input_data.columns:
        input_data['slope_downsloping'] = 1

    # Thal
    if thal == "fixed defect" and 'thal_fixed defect' in input_data.columns:
        input_data['thal_fixed defect'] = 1
    elif thal == "reversable defect" and 'thal_reversable defect' in input_data.columns:
        input_data['thal_reversable defect'] = 1

    # =========================
    # PREDICT
    # =========================

    prediction = model.predict(input_data)

    st.subheader("Result")

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease")