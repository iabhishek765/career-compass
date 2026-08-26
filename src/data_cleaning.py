import pandas as pd


# --------------------------------------------------
# Load Raw Dataset
# --------------------------------------------------

DATA_PATH = "data/student_placement_data.csv"

df = pd.read_csv(
    DATA_PATH,
    keep_default_na=False
)


# --------------------------------------------------
# Create a Copy of the Raw Dataset
# --------------------------------------------------

cleaned_df = df.copy()


# --------------------------------------------------
# Display Basic Information
# --------------------------------------------------

print("=" * 60)
print("CAREER COMPASS - DATA CLEANING")
print("=" * 60)

print("\nRaw Dataset Loaded Successfully!")

print(f"\nNumber of Rows: {cleaned_df.shape[0]}")
print(f"Number of Columns: {cleaned_df.shape[1]}")

print("\nFirst 5 Records:")

print(cleaned_df.head())

# --------------------------------------------------
# Check and Remove Duplicate Records
# --------------------------------------------------

print("\nChecking for duplicate records...")

duplicate_count = cleaned_df.duplicated().sum()

print(f"Duplicate Records Found: {duplicate_count}")


# Remove duplicate records
cleaned_df = cleaned_df.drop_duplicates().reset_index(drop=True)


print(f"Rows After Duplicate Removal: {cleaned_df.shape[0]}")

# --------------------------------------------------
# Check Missing Values
# --------------------------------------------------

print("\nChecking for missing values...")


# Calculate missing values for each column
missing_values = cleaned_df.isnull().sum()


# Display only columns containing missing values
columns_with_missing_values = missing_values[
    missing_values > 0
]


if len(columns_with_missing_values) == 0:

    print("No missing values found in the dataset.")

else:

    print("\nColumns with missing values:")

    print(columns_with_missing_values)


# Display total missing values
total_missing_values = cleaned_df.isnull().sum().sum()

print(f"\nTotal Missing Values: {total_missing_values}")

# --------------------------------------------------
# Validate Numerical Feature Ranges
# --------------------------------------------------

print("\nValidating numerical feature ranges...")


# Define valid ranges for important numerical features
numerical_ranges = {
    "Age": (18, 30),
    "CGPA": (0, 10),
    "LeetCode_Problems": (0, 2000),
    "GitHub_Repositories": (0, 100),
    "Total_Projects": (0, 50),
    "AI_ML_Projects": (0, 50),
    "Internship_Count": (0, 10),
    "Industry_Certifications": (0, 50)
}


# Check each numerical feature
for column, (minimum, maximum) in numerical_ranges.items():

    invalid_records = cleaned_df[
        ~cleaned_df[column].between(minimum, maximum)
    ]

    if len(invalid_records) == 0:

        print(f"{column}: Valid")

    else:

        print(
            f"{column}: "
            f"{len(invalid_records)} invalid records found"
        )


print("\nNumerical feature validation completed.")

# --------------------------------------------------
# Validate Logical Consistency Between Features
# --------------------------------------------------

print("\nValidating logical consistency...")


# Check 1:
# AI/ML projects should not exceed total projects

invalid_ai_ml_projects = cleaned_df[
    cleaned_df["AI_ML_Projects"] > cleaned_df["Total_Projects"]
]

print(
    f"AI/ML Projects > Total Projects: "
    f"{len(invalid_ai_ml_projects)} invalid records"
)


# Check 2:
# Students with zero internships should have domain as None

invalid_zero_internships = cleaned_df[
    (cleaned_df["Internship_Count"] == 0)
    &
    (cleaned_df["Internship_Domain"] != "None")
]

print(
    f"Zero Internships with Invalid Domain: "
    f"{len(invalid_zero_internships)} invalid records"
)


# Check 3:
# Students with internships should not have domain as None

invalid_internship_domain = cleaned_df[
    (cleaned_df["Internship_Count"] > 0)
    &
    (cleaned_df["Internship_Domain"] == "None")
]

print(
    f"Internships Present but Domain is None: "
    f"{len(invalid_internship_domain)} invalid records"
)


# Check 4:
# GitHub profile consistency

invalid_github_profile = cleaned_df[
    (cleaned_df["GitHub_Repositories"] > 0)
    &
    (cleaned_df["GitHub_Profile"] == "No")
]

print(
    f"GitHub Repositories Present but Profile is No: "
    f"{len(invalid_github_profile)} invalid records"
)


print("\nLogical consistency validation completed.")

# --------------------------------------------------
# Validate Categorical Feature Values
# --------------------------------------------------

print("\nValidating categorical feature values...")


# Define valid categories
valid_categories = {

    "DSA_Level": [
        "Beginner",
        "Intermediate",
        "Advanced"
    ],

    "Major_Project_Level": [
        "Basic",
        "Intermediate",
        "Advanced"
    ],

    "Python_Level": [
        "None",
        "Beginner",
        "Intermediate",
        "Advanced"
    ],

    "SQL_Level": [
        "None",
        "Beginner",
        "Intermediate",
        "Advanced"
    ],

    "PowerBI_Level": [
        "None",
        "Beginner",
        "Intermediate",
        "Advanced"
    ],

    "MachineLearning_Level": [
        "None",
        "Beginner",
        "Intermediate",
        "Advanced"
    ],

    "Statistics_Level": [
        "None",
        "Beginner",
        "Intermediate",
        "Advanced"
    ],

    "DeepLearning_Level": [
        "None",
        "Beginner",
        "Intermediate",
        "Advanced"
    ],

    "Communication_Level": [
        "Poor",
        "Average",
        "Good",
        "Excellent"
    ],

    "Placement_Status": [
        "Placed",
        "Not Placed"
    ]
}


# Check each categorical feature
for column, allowed_values in valid_categories.items():

    invalid_values = cleaned_df[
        ~cleaned_df[column].isin(allowed_values)
    ]

    if len(invalid_values) == 0:

        print(f"{column}: Valid")

    else:

        print(
            f"{column}: "
            f"{len(invalid_values)} invalid records found"
        )


print("\nCategorical feature validation completed.")

# --------------------------------------------------
# Save Cleaned Dataset
# --------------------------------------------------

CLEANED_DATA_PATH = "data/cleaned_student_placement_data.csv"


cleaned_df.to_csv(
    CLEANED_DATA_PATH,
    index=False
)


print("\n" + "=" * 60)

print("DATA CLEANING COMPLETED SUCCESSFULLY")

print("=" * 60)


print(f"\nCleaned Dataset Saved To: {CLEANED_DATA_PATH}")

print(f"\nFinal Number of Rows: {cleaned_df.shape[0]}")

print(f"Final Number of Columns: {cleaned_df.shape[1]}")