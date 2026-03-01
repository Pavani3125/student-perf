import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data.csv")

X = data[['Hours_Studied', 'Attendance', 'Previous_Score', 'Assignments']]
y = data['Final_Score']

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# ----------- WEB PAGE DESIGN -----------

st.title("🎓 Student Performance Predictor")

st.write("Enter student details below:")

hours = st.number_input("Study Hours", min_value=0.0)
attendance = st.number_input("Attendance (%)", min_value=0.0)
previous = st.number_input("Previous Score", min_value=0.0)
assignments = st.number_input("Assignments Completed", min_value=0.0)

if st.button("Predict Final Score"):
    prediction = model.predict([[hours, attendance, previous, assignments]])
    st.success(f"Predicted Final Score: {prediction[0]:.2f}")