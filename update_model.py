import joblib
from datetime import datetime

joblib.dump(model, 'model.pkl')

# Load
model = joblib.load('model.pkl')

# 2. Add your custom update logic here
print(f"Model loaded successfully at {datetime.now()}")
# Example: model.fit(new_data, new_labels)

# 3. Save the model (uncomment when ready)
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)
