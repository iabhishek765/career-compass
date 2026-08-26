# ============================================================
# Career Compass
# Machine Learning Preprocessing Pipeline
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# ------------------------------------------------------------
# 1. Load Cleaned Dataset
# ------------------------------------------------------------

DATA_PATH = "data/cleaned_student_placement_data.csv"

df = pd.read_csv(
    DATA_PATH,
    keep_default_na=False
)


print("=" * 60)
print("MACHINE LEARNING PREPROCESSING")
print("=" * 60)

print("\nDataset loaded successfully.")

print(f"\nNumber of Rows: {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")


# ------------------------------------------------------------
# 2. Separate Input Features and Target Variable
# ------------------------------------------------------------

# Define target variable
TARGET_COLUMN = "Placement_Status"


# Define columns that must not be used for model training
EXCLUDED_FEATURES = [
    "Student_ID",
    "Placement_Score",
    TARGET_COLUMN
]


# Create input feature matrix
X = df.drop(
    columns=EXCLUDED_FEATURES
)


# Create target variable
y = df[TARGET_COLUMN]


# ------------------------------------------------------------
# Display Feature Selection Information
# ------------------------------------------------------------

print("\n" + "=" * 60)

print("FEATURE SELECTION")

print("=" * 60)


print("\nExcluded Features:")

for feature in EXCLUDED_FEATURES:
    print(f"- {feature}")


print("\nInput Feature Matrix Shape:")

print(X.shape)


print("\nTarget Variable Shape:")

print(y.shape)


print("\nInput Features Used for Modeling:")

for index, feature in enumerate(X.columns, start=1):
    print(f"{index}. {feature}")


# ------------------------------------------------------------
# Target Leakage Safety Check
# ------------------------------------------------------------

assert "Placement_Score" not in X.columns, (
    "TARGET LEAKAGE ERROR: Placement_Score is present in X!"
)

assert "Placement_Status" not in X.columns, (
    "TARGET LEAKAGE ERROR: Placement_Status is present in X!"
)

assert "Student_ID" not in X.columns, (
    "FEATURE ERROR: Student_ID is present in X!"
)


print("\nTarget leakage safety check passed successfully!")


# ------------------------------------------------------------
# 3. Identify Numerical and Categorical Features
# ------------------------------------------------------------

numerical_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()


categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()


# ------------------------------------------------------------
# Display Feature Type Information
# ------------------------------------------------------------

print("\n" + "=" * 60)

print("FEATURE TYPE IDENTIFICATION")

print("=" * 60)


print(
    f"\nNumber of Numerical Features: "
    f"{len(numerical_features)}"
)

print("\nNumerical Features:")

for index, feature in enumerate(
    numerical_features,
    start=1
):
    print(f"{index}. {feature}")


print(
    f"\nNumber of Categorical Features: "
    f"{len(categorical_features)}"
)

print("\nCategorical Features:")

for index, feature in enumerate(
    categorical_features,
    start=1
):
    print(f"{index}. {feature}")


# ------------------------------------------------------------
# Feature Count Safety Check
# ------------------------------------------------------------

total_identified_features = (
    len(numerical_features)
    + len(categorical_features)
)


assert total_identified_features == X.shape[1], (
    "FEATURE IDENTIFICATION ERROR: "
    "Not all input features were identified!"
)


print(
    "\nAll input features identified successfully!"
)

# ------------------------------------------------------------
# 4. Split Dataset into Training and Testing Sets
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ------------------------------------------------------------
# Display Train-Test Split Information
# ------------------------------------------------------------

print("\n" + "=" * 60)

print("TRAIN-TEST SPLIT")

print("=" * 60)


print("\nTraining Feature Shape:")
print(X_train.shape)


print("\nTesting Feature Shape:")
print(X_test.shape)


print("\nTraining Target Shape:")
print(y_train.shape)


print("\nTesting Target Shape:")
print(y_test.shape)


# ------------------------------------------------------------
# Check Target Distribution
# ------------------------------------------------------------

print("\nTraining Target Distribution (%):")

print(
    y_train
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


print("\nTesting Target Distribution (%):")

print(
    y_test
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


# ------------------------------------------------------------
# Split Safety Checks
# ------------------------------------------------------------

assert len(X_train) == len(y_train), (
    "ERROR: X_train and y_train sizes do not match!"
)

assert len(X_test) == len(y_test), (
    "ERROR: X_test and y_test sizes do not match!"
)


print("\nTrain-test split completed successfully!")

# ------------------------------------------------------------
# 5. Create Machine Learning Preprocessing Pipeline
# ------------------------------------------------------------

# Numerical feature preprocessing
numerical_transformer = StandardScaler()


# Categorical feature preprocessing
categorical_transformer = OneHotEncoder(
    handle_unknown="ignore"
)


# Combine numerical and categorical preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "numerical",
            numerical_transformer,
            numerical_features
        ),
        (
            "categorical",
            categorical_transformer,
            categorical_features
        )
    ]
)


# ------------------------------------------------------------
# Display Preprocessing Configuration
# ------------------------------------------------------------

print("\n" + "=" * 60)

print("PREPROCESSING PIPELINE")

print("=" * 60)


print("\nNumerical Feature Transformation:")
print("StandardScaler")


print("\nCategorical Feature Transformation:")
print("OneHotEncoder")


print("\nUnknown Category Handling:")
print("Ignore unknown categories")


print("\nPreprocessing pipeline created successfully!")

# ------------------------------------------------------------
# 6. Fit Preprocessor and Transform Data
# ------------------------------------------------------------

# Fit the preprocessor only on training data
# and transform the training data

X_train_processed = preprocessor.fit_transform(
    X_train
)


# Transform testing data using the already-fitted preprocessor

X_test_processed = preprocessor.transform(
    X_test
)


# ------------------------------------------------------------
# Display Processed Data Information
# ------------------------------------------------------------

print("\n" + "=" * 60)

print("DATA TRANSFORMATION")

print("=" * 60)


print("\nOriginal Training Data Shape:")

print(X_train.shape)


print("\nProcessed Training Data Shape:")

print(X_train_processed.shape)


print("\nOriginal Testing Data Shape:")

print(X_test.shape)


print("\nProcessed Testing Data Shape:")

print(X_test_processed.shape)


# ------------------------------------------------------------
# Transformation Safety Checks
# ------------------------------------------------------------

assert X_train_processed.shape[0] == X_train.shape[0], (
    "ERROR: Training row count changed during preprocessing!"
)


assert X_test_processed.shape[0] == X_test.shape[0], (
    "ERROR: Testing row count changed during preprocessing!"
)


assert X_train_processed.shape[1] == X_test_processed.shape[1], (
    "ERROR: Training and testing feature counts do not match!"
)


print("\nData transformation completed successfully!")