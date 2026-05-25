import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# -------------------------
# LOAD DATA
# -------------------------

df = pd.read_csv("data/cleaned_data/reliance_cleaned.csv")

# -------------------------
# FEATURE SELECTION
# -------------------------

X = df[['Open', 'High', 'Low', 'Volume']]

y = df['Close']

# -------------------------
# TRAIN TEST SPLIT
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# MODEL CREATION
# -------------------------

model = LinearRegression()

# -------------------------
# MODEL TRAINING
# -------------------------

model.fit(X_train, y_train)

# -------------------------
# PREDICTION
# -------------------------

predictions = model.predict(X_test)

# -------------------------
# EVALUATION
# -------------------------

mae = mean_absolute_error(y_test, predictions)

print("\n===== MODEL PERFORMANCE =====")

print("Mean Absolute Error:", mae)

# -------------------------
# SAMPLE PREDICTIONS
# -------------------------

result = pd.DataFrame({
    'Actual Price': y_test.values,
    'Predicted Price': predictions
})

print("\n===== SAMPLE PREDICTIONS =====")

print(result.head())

# -------------------------
# FUTURE PREDICTION
# -------------------------

sample_data = pd.DataFrame({
    'Open': [1400],
    'High': [1415],
    'Low': [1395],
    'Volume': [5000000]
})

future_prediction = model.predict(sample_data)

print("\nPredicted Closing Price:", future_prediction[0])
