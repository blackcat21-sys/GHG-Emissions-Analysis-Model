# 🚗 GHG Emission Level Predictor

A machine learning-powered Streamlit web app that predicts the greenhouse gas (GHG) emission level of a vehicle based on environmental and mechanical parameters.

---

## 📌 Project Overview

This project helps estimate a vehicle's GHG emission level — categorized as Low, Medium, or High — using a trained Random Forest Classifier. It uses features such as engine size, fuel type, mileage, CO₂/NOₓ/PM2.5 emissions, and driving conditions.

The goal is to support sustainability monitoring and real-time emission feedback in applications such as smart transportation, policy simulation, or fleet management systems.

---

## 🧠 Model Details

- 🎯 Target: Emission Level (Low, Medium, High)
- 🧰 Algorithm: Random Forest Classifier
- ⚙️ Accuracy: 100% (on test data)
- ✅ Categorical Encoding: One-hot encoding
- 📊 Feature Scaling: StandardScaler

---

## 🖥️ Streamlit App Features

- 🚘 Input fields for vehicle specifications
- 📊 Predicts emission level based on user input
- ✅ Works in real-time with live feedback
- 📦 Model trained on a dataset of 10,000 vehicles with multiple emissions metrics

---

## 🛠 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/blackcat21-cys/ghg-emission-predictor.git
cd GHG-Emmissions-Analysis-Model
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the app:

```bash
streamlit run app.py
```

---

## 📁 Files

| File                     | Description                              |
|--------------------------|------------------------------------------|
| app.py                   | Streamlit web app                        |
| emission_level_model.pkl | Trained Random Forest model              |
| feature_scaler.pkl       | Scaler used for preprocessing            |
| feature_names.pkl        | List of features used during training    |
| GHG_emission_dataset.csv | (optional) Original dataset              |

---

## 📦 Dependencies

- streamlit  
- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn  
- joblib

To install manually:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib
```

---

## 📷 Sample Predictions

Try it out with sample inputs for:

- ✅ Low: Electric Motorcycle with low CO₂ and NOx  
- 🔶 Medium: Modern Diesel Truck with moderate emissions  
- 🔴 High: Old Petrol Truck with high CO₂ and NOx

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Developed by [Priyanshu Kumar] 
B.Tech CSE - VIT Bhopal  
GHG Emission Modeling | Machine Learning | Cloud Deployment
