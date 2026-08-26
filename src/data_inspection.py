import pandas as pd


# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

DATA_PATH = "data/student_placement_data.csv"

df = pd.read_csv(
    DATA_PATH,
    keep_default_na=False
)

print("=" * 60)
print("CAREER COMPASS - DATASET INSPECTION")
print("=" * 60)


# --------------------------------------------------
# Dataset Shape
# --------------------------------------------------

print("\n1. DATASET SHAPE")

print(f"Number of Rows: {df.shape[0]}")
print(f"Number of Columns: {df.shape[1]}")


# --------------------------------------------------
# First 5 Records
# --------------------------------------------------

print("\n2. FIRST 5 RECORDS")

print(df.head())


# --------------------------------------------------
# Column Names
# --------------------------------------------------

print("\n3. COLUMN NAMES")

for index, column in enumerate(df.columns, start=1):
    print(f"{index}. {column}")


# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

print("\n4. DATASET INFORMATION")

df.info()


# --------------------------------------------------
# Data Types
# --------------------------------------------------

print("\n5. DATA TYPES")

print(df.dtypes)

# --------------------------------------------------
# Missing Values
# --------------------------------------------------

print("\n6. MISSING VALUES")

missing_values = df.isnull().sum()

print(missing_values)


print("\nTotal Missing Values:")

print(df.isnull().sum().sum())


# --------------------------------------------------
# Missing Value Percentage
# --------------------------------------------------

print("\n7. MISSING VALUE PERCENTAGE")

missing_percentage = (
    df.isnull().sum() / len(df)
) * 100

print(missing_percentage.round(2))


# --------------------------------------------------
# Duplicate Records
# --------------------------------------------------

print("\n8. DUPLICATE RECORDS")

duplicate_count = df.duplicated().sum()

print(f"Number of Duplicate Records: {duplicate_count}")


# --------------------------------------------------
# Descriptive Statistics for Numerical Features
# --------------------------------------------------

print("\n9. NUMERICAL FEATURE STATISTICS")

numerical_statistics = df.describe()

print(numerical_statistics)


# --------------------------------------------------
# Minimum and Maximum Values
# --------------------------------------------------

print("\n10. NUMERICAL FEATURE RANGES")

numerical_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns

for column in numerical_columns:

    print(
        f"{column}: "
        f"Min = {df[column].min()}, "
        f"Max = {df[column].max()}, "
        f"Mean = {df[column].mean():.2f}"
    )


    # --------------------------------------------------
# Inspect Categorical Features
# --------------------------------------------------

print("\n11. CATEGORICAL FEATURE INSPECTION")

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

print(f"\nNumber of Categorical Columns: {len(categorical_columns)}")


for column in categorical_columns:

    print("\n" + "-" * 50)

    print(f"Column: {column}")

    print(f"Unique Values: {df[column].nunique()}")

    print("Categories:")

    print(df[column].value_counts())