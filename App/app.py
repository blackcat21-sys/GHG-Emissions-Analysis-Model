# app.py

import streamlit as st
import pandas as pd
import joblib

# Load saved model and scaler
model = joblib.load("emission_level_model.pkl")
scaler = joblib.load("feature_scaler.pkl")

# App title
st.title("🚗 GHG Emission Level Predictor")

# Collect user input
st.header("📋 Enter Vehicle Details")

vehicle_type = st.selectbox("Vehicle Type", ['Car', 'Motorcycle', 'Truck', 'Bus'])
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Hybrid', 'Electric'])
road_type = st.selectbox("Road Type", ['Highway', 'City', 'Rural'])
traffic_conditions = st.selectbox("Traffic Conditions", ['Free flow', 'Moderate', 'Heavy'])

engine_size = st.number_input("Engine Size (L)", min_value=0.5, max_value=10.0, step=0.1)
age_of_vehicle = st.number_input("Age of Vehicle (years)", min_value=0, max_value=30)
mileage = st.number_input("Mileage (km)", min_value=0)
speed = st.number_input("Speed (km/h)", min_value=0)
acceleration = st.number_input("Acceleration (m/s²)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=-30.0, max_value=50.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0)
air_pressure = st.number_input("Air Pressure (hPa)", min_value=800.0, max_value=1100.0)

# Optional: Emission estimates if available
co2 = st.number_input("CO2 Emissions (g/km)", min_value=0.0)
nox = st.number_input("NOx Emissions (g/km)", min_value=0.0)
pm25 = st.number_input("PM2.5 Emissions (g/km)", min_value=0.0)
voc = st.number_input("VOC Emissions (g/km)", min_value=0.0)
so2 = st.number_input("SO2 Emissions (g/km)", min_value=0.0)

# Create DataFrame from inputs
input_dict = {
    'Engine Size': engine_size,
    'Age of Vehicle': age_of_vehicle,
    'Mileage': mileage,
    'Speed': speed,
    'Acceleration': acceleration,
    'Temperature': temperature,
    'Humidity': humidity,
    'Wind Speed': wind_speed,
    'Air Pressure': air_pressure,
    'CO2 Emissions': co2,
    'NOx Emissions': nox,
    'PM2.5 Emissions': pm25,
    'VOC Emissions': voc,
    'SO2 Emissions': so2,
    f'Vehicle Type_{vehicle_type}': 1,
    f'Fuel Type_{fuel_type}': 1,
    f'Road Type_{road_type}': 1,
    f'Traffic Conditions_{traffic_conditions}': 1
}

# Get full feature list (from training)
full_features = joblib.load("feature_names.pkl")  # save X.columns as this file earlier
input_df = pd.DataFrame([input_dict])
for col in full_features:
    if col not in input_df.columns:
        input_df[col] = 0  # fill missing dummy columns

# Reorder columns and scale
input_df = input_df[full_features]
scaled_input = scaler.transform(input_df)

# Predict
if st.button("Predict Emission Level"):
    prediction = model.predict(scaled_input)[0]
    st.success(f"📊 Predicted Emission Level: {prediction}")
