import joblib
from sklearn.tree import DecisionTreeClassifier  # Replace with your actual model class

try:
    # Try loading existing model
    model = joblib.load('model.pkl')
except:
    print("No existing model found, creating new one")
    model = DecisionTreeClassifier()  # Fallback to new model



# Save the updated model
joblib.dump(model, 'model.pkl')
print("Model updated successfully")
