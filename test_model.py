import joblib
import sklearn

print("Scikit-learn Version:", sklearn.__version__)

model = joblib.load("hotel_booking_model.pkl")

print(type(model))
print("Model Loaded Successfully ✅")