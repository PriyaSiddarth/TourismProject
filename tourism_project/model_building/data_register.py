import pandas as pd

# Load the raw dataset
df = pd.read_csv('tourism_project/data/tourism.csv')

# Validate that the expected columns are present before registering it
expected_columns = [
    "NumberOfTrips", "NumberOfChildrenVisiting", "MonthlyIncome", "Designation",
    "Occupation", "CityTier", "DurationOfPitch", "Passport", "PitchSatisfactionScore", "ProductPitched"
]
missing = [c for c in expected_columns if c not in df.columns]
if missing:
    raise ValueError(f"Dataset is missing expected columns: {missing}")

print("Dataset registered successfully.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("Columns:", list(df.columns))
print("Customer purchase distribution:")
print(df["ProdTaken"].value_counts())
