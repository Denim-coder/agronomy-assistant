import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Load dataset
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'plant_health_data.csv')
df = pd.read_csv(data_path)

# Drop unnecessary columns if any (like Timestamp, Plant_ID)
df.drop(columns=['Timestamp', 'Plant_ID'], inplace=True, errors='ignore')

# Features and Target
X = df.drop('Plant_Health_Status', axis=1)
y = df['Plant_Health_Status']

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and preprocessors
model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
os.makedirs(model_dir, exist_ok=True)

joblib.dump(model, os.path.join(model_dir, 'health_model.pkl'))
joblib.dump(scaler, os.path.join(model_dir, 'health_scaler.pkl'))
joblib.dump(label_encoder, os.path.join(model_dir, 'health_label_encoder.pkl'))

print("✅ Model, scaler, and label encoder saved successfully!")
