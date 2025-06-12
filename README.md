# 🌾 AI-Powered Agronomy Assistant

An intelligent farm support system built using **Python**, **Flask**, and **Streamlit**, designed to assist farmers and agronomists with **real-time insights**, **crop health diagnostics**, and **actionable recommendations** based on weather, soil, and satellite data.

---

## 🚀 Live Demo

👉 **Streamlit App:** [Click Here to Try It](https://your-streamlit-app-url-here.streamlit.app)  
👉 **Backend API:** [Flask API on Render](https://your-flask-api-url.onrender.com)

---

## 🧠 Features

- 🌦️ **Weather Insights** — Real-time weather data for your location
- 🌱 **Crop Recommendation System** — Suggests the best crops based on soil and climate
- 🐛 **Crop Disease & Pest Risk Prediction** — Predicts risk using machine learning
- 💧 **Irrigation Alerts** — Notifies when soil moisture is low
- 🧪 **Sensor Integration** — Ready to plug into real-time IoT soil sensor data
- 🧾 **Field Health Dashboard** — Visual summary of crop and irrigation status
- 📬 **Farmer Feedback & Notifications** — Capture user input and alert responses

---

## 🛠️ Tech Stack

| Layer        | Tools Used                       |
|--------------|----------------------------------|
| Frontend     | Streamlit                        |
| Backend      | Flask (REST API)                 |
| ML/AI        | Scikit-learn, Pandas, NumPy      |
| Data Sources | Weather API, Simulated Soil Data |
| Deployment   | Streamlit Cloud + Render         |
| Version Ctrl | Git & GitHub                     |

---

## 📁 Project Structure


agronomy-assistant/
├── app/ # Flask backend routes
│ ├── init.py
│ └── routes.py
├── models/ # Trained ML models
├── streamlit_app.py # Streamlit frontend
├── main.py # Flask app runner
├── requirements.txt
├── README.md
└── ...



---

## ⚙️ How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/Denim-coder/agronomy-assistant.git
   cd agronomy-assistant


Install dependencies:
pip install -r requirements.txt


Run Flask API:
python main.py

In another terminal, run Streamlit:
streamlit run streamlit_app.py


📌 Highlights
> Real-time recommendations for farmers

> Easy-to-use UI for non-technical users

> Fully deployed on cloud platforms

> Scalable architecture with separate API & UI layers



📄 License
This project is open-source under the MIT License.



---

### ✅ What You Need to Do

1. Replace:
   - `https://your-streamlit-app-url-here.streamlit.app`
   - `https://your-flask-api-url.onrender.com`
   - `https://your-demo-video-link.com`

2. Copy this into your `README.md` file in the root of your GitHub repo

3. Commit and push:
   ```bash
   git add README.md
   git commit -m "Updated README with project description and demo link"
   git push
