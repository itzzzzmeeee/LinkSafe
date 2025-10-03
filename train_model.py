import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
from feature_extraction import basic_features

# Load dataset
df = pd.read_csv("urls_dataset.csv")

# Extract features
X = pd.DataFrame([basic_features(u) for u in df["url"]])
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
joblib.dump({"model": clf}, "phish_detector.joblib")
print("Model saved as phish_detector.joblib")
