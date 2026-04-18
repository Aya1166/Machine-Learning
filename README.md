# ❤️ Heart Disease Prediction

## 👨‍🎓 Author
- Aya loghmari

---

## 🎯 Project Objective

The goal of this project is to build a Machine Learning model capable of predicting whether a patient has a heart disease based on medical data.

This project follows the full Data Science pipeline:
- Data analysis
- Preprocessing
- Modeling
- Evaluation
- Deployment (Streamlit)

---

## 📊 Dataset

- Source: Kaggle - Heart Disease Dataset
- Type: Medical structured data
- Number of samples: ~1000
- Features: Age, cholesterol, blood pressure, etc.
- Target variable: `num`
  - 0 → No disease
  - 1 → Disease

---

## ❓ Problem Type

- Supervised Learning
- Binary Classification

---

## 🔍 Project Steps

### 1. Exploratory Data Analysis (EDA)
- Data structure analysis
- Statistical summary
- Distribution visualization
- Correlation heatmap
- Missing values detection

### 2. Data Preprocessing
- Target transformation (multi-class → binary)
- Encoding categorical variables (One-Hot Encoding)
- Feature scaling (Standardization)
- Class balance verification

### 3. Modeling
Models used:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Random Forest

### 4. Evaluation
Metrics used:
- Accuracy
- Precision
- Recall
- F1-score

Best model: **Random Forest**

### 5. Optimization
- Hyperparameter tuning using GridSearchCV

---

## 📈 Results

Random Forest achieved the best performance due to its ability to capture complex relationships in the data.

---

## 🚀 Application

A Streamlit web application was developed to:
- Input patient data
- Predict heart disease
- Display results in real-time

---

## ⚠️ Disclaimer

This model is intended as a decision-support tool and does NOT replace professional medical diagnosis.

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
