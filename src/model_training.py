# ============================================================
# Career Compass
# Machine Learning Model Training
# ============================================================

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import make_scorer 

import joblib


from sklearn.model_selection import GridSearchCV


from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# ------------------------------------------------------------
# 1. Load Cleaned Dataset
# ------------------------------------------------------------

DATA_PATH = "data/cleaned_student_placement_data.csv"

df = pd.read_csv(
    DATA_PATH,
    keep_default_na=False
)


print("=" * 60)
print("CAREER COMPASS - MODEL TRAINING")
print("=" * 60)

print("\nDataset loaded successfully.")

print(f"\nDataset Shape: {df.shape}")


# ------------------------------------------------------------
# 2. Define Target and Excluded Features
# ------------------------------------------------------------

TARGET_COLUMN = "Placement_Status"

EXCLUDED_FEATURES = [
    "Student_ID",
    "Placement_Score",
    TARGET_COLUMN
]


# ------------------------------------------------------------
# 3. Create Input Features and Target
# ------------------------------------------------------------

X = df.drop(
    columns=EXCLUDED_FEATURES
)

y = df[TARGET_COLUMN]


print("\nInput Feature Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)


# ------------------------------------------------------------
# 4. Target Leakage Safety Checks
# ------------------------------------------------------------

assert "Placement_Score" not in X.columns, (
    "TARGET LEAKAGE ERROR: Placement_Score found in model inputs!"
)

assert "Placement_Status" not in X.columns, (
    "TARGET LEAKAGE ERROR: Placement_Status found in model inputs!"
)

assert "Student_ID" not in X.columns, (
    "FEATURE ERROR: Student_ID found in model inputs!"
)


print("\nTarget leakage safety checks passed successfully!")


# ------------------------------------------------------------
# 5. Train-Test Split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)


print("\nModel training environment prepared successfully!")


# ------------------------------------------------------------
# 6. Identify Numerical and Categorical Features
# ------------------------------------------------------------

numerical_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object"]
).columns.tolist()


print("\n" + "=" * 60)
print("FEATURE PREPROCESSING CONFIGURATION")
print("=" * 60)

print(f"\nNumber of Numerical Features: {len(numerical_features)}")
print(f"Number of Categorical Features: {len(categorical_features)}")


# ------------------------------------------------------------
# 7. Create Preprocessing Pipeline
# ------------------------------------------------------------

numerical_transformer = StandardScaler()

categorical_transformer = OneHotEncoder(
    handle_unknown="ignore"
)


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


print("\nNumerical Preprocessing: StandardScaler")
print("Categorical Preprocessing: OneHotEncoder")

print("\nModel preprocessing configuration created successfully!")


# ------------------------------------------------------------
# 8. Create Logistic Regression Pipeline
# ------------------------------------------------------------

logistic_pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                random_state=42
            )
        )
    ]
)


print("\n" + "=" * 60)
print("LOGISTIC REGRESSION BASELINE MODEL")
print("=" * 60)

print("\nModel pipeline created successfully!")


# ------------------------------------------------------------
# 9. Train Logistic Regression Model
# ------------------------------------------------------------

print("\nTraining Logistic Regression model...")

logistic_pipeline.fit(
    X_train,
    y_train
)

print("\nLogistic Regression model trained successfully!")

# ------------------------------------------------------------
# 10. Generate Predictions
# ------------------------------------------------------------

logistic_predictions = logistic_pipeline.predict(
    X_test
)


print("\nPredictions generated successfully!")


# ------------------------------------------------------------
# 11. Evaluate Logistic Regression Model
# ------------------------------------------------------------

logistic_accuracy = accuracy_score(
    y_test,
    logistic_predictions
)

logistic_precision = precision_score(
    y_test,
    logistic_predictions,
    pos_label="Placed"
)

logistic_recall = recall_score(
    y_test,
    logistic_predictions,
    pos_label="Placed"
)

logistic_f1 = f1_score(
    y_test,
    logistic_predictions,
    pos_label="Placed"
)


print("\n" + "=" * 60)

print("LOGISTIC REGRESSION MODEL EVALUATION")

print("=" * 60)


print(f"\nAccuracy:  {logistic_accuracy:.4f}")

print(f"Precision: {logistic_precision:.4f}")

print(f"Recall:    {logistic_recall:.4f}")

print(f"F1 Score:  {logistic_f1:.4f}")


# ------------------------------------------------------------
# 12. Classification Report
# ------------------------------------------------------------

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        logistic_predictions
    )
)


# ------------------------------------------------------------
# 13. Confusion Matrix
# ------------------------------------------------------------

logistic_confusion_matrix = confusion_matrix(
    y_test,
    logistic_predictions,
    labels=[
        "Not Placed",
        "Placed"
    ]
)


print("\nConfusion Matrix:")

print(logistic_confusion_matrix)

# ------------------------------------------------------------
# 14. Create Decision Tree Pipeline
# ------------------------------------------------------------

decision_tree_pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            DecisionTreeClassifier(
                random_state=42
            )
        )
    ]
)


print("\n" + "=" * 60)
print("DECISION TREE MODEL")
print("=" * 60)


# ------------------------------------------------------------
# 15. Train Decision Tree Model
# ------------------------------------------------------------

print("\nTraining Decision Tree model...")

decision_tree_pipeline.fit(
    X_train,
    y_train
)

print("\nDecision Tree model trained successfully!")


# ------------------------------------------------------------
# 16. Generate Predictions
# ------------------------------------------------------------

decision_tree_predictions = decision_tree_pipeline.predict(
    X_test
)


# ------------------------------------------------------------
# 17. Evaluate Decision Tree Model
# ------------------------------------------------------------

decision_tree_accuracy = accuracy_score(
    y_test,
    decision_tree_predictions
)

decision_tree_precision = precision_score(
    y_test,
    decision_tree_predictions,
    pos_label="Placed"
)

decision_tree_recall = recall_score(
    y_test,
    decision_tree_predictions,
    pos_label="Placed"
)

decision_tree_f1 = f1_score(
    y_test,
    decision_tree_predictions,
    pos_label="Placed"
)


print("\n" + "=" * 60)
print("DECISION TREE MODEL EVALUATION")
print("=" * 60)

print(f"\nAccuracy:  {decision_tree_accuracy:.4f}")
print(f"Precision: {decision_tree_precision:.4f}")
print(f"Recall:    {decision_tree_recall:.4f}")
print(f"F1 Score:  {decision_tree_f1:.4f}")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        decision_tree_predictions
    )
)


decision_tree_confusion_matrix = confusion_matrix(
    y_test,
    decision_tree_predictions,
    labels=[
        "Not Placed",
        "Placed"
    ]
)

print("\nConfusion Matrix:")

print(decision_tree_confusion_matrix)

# ------------------------------------------------------------
# 18. Create Random Forest Pipeline
# ------------------------------------------------------------

random_forest_pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                n_jobs=-1
            )
        )
    ]
)


print("\n" + "=" * 60)
print("RANDOM FOREST MODEL")
print("=" * 60)


# ------------------------------------------------------------
# 19. Train Random Forest Model
# ------------------------------------------------------------

print("\nTraining Random Forest model...")

random_forest_pipeline.fit(
    X_train,
    y_train
)

print("\nRandom Forest model trained successfully!")


# ------------------------------------------------------------
# 20. Generate Predictions
# ------------------------------------------------------------

random_forest_predictions = random_forest_pipeline.predict(
    X_test
)


# ------------------------------------------------------------
# 21. Evaluate Random Forest Model
# ------------------------------------------------------------

random_forest_accuracy = accuracy_score(
    y_test,
    random_forest_predictions
)

random_forest_precision = precision_score(
    y_test,
    random_forest_predictions,
    pos_label="Placed"
)

random_forest_recall = recall_score(
    y_test,
    random_forest_predictions,
    pos_label="Placed"
)

random_forest_f1 = f1_score(
    y_test,
    random_forest_predictions,
    pos_label="Placed"
)


print("\n" + "=" * 60)
print("RANDOM FOREST MODEL EVALUATION")
print("=" * 60)

print(f"\nAccuracy:  {random_forest_accuracy:.4f}")
print(f"Precision: {random_forest_precision:.4f}")
print(f"Recall:    {random_forest_recall:.4f}")
print(f"F1 Score:  {random_forest_f1:.4f}")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        random_forest_predictions
    )
)


random_forest_confusion_matrix = confusion_matrix(
    y_test,
    random_forest_predictions,
    labels=[
        "Not Placed",
        "Placed"
    ]
)


print("\nConfusion Matrix:")

print(random_forest_confusion_matrix)


# ------------------------------------------------------------
# 22. Create Gradient Boosting Pipeline
# ------------------------------------------------------------

gradient_boosting_pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            GradientBoostingClassifier(
                random_state=42
            )
        )
    ]
)


print("\n" + "=" * 60)
print("GRADIENT BOOSTING MODEL")
print("=" * 60)


# ------------------------------------------------------------
# 23. Train Gradient Boosting Model
# ------------------------------------------------------------

print("\nTraining Gradient Boosting model...")

gradient_boosting_pipeline.fit(
    X_train,
    y_train
)

print("\nGradient Boosting model trained successfully!")


# ------------------------------------------------------------
# 24. Generate Predictions
# ------------------------------------------------------------

gradient_boosting_predictions = gradient_boosting_pipeline.predict(
    X_test
)


# ------------------------------------------------------------
# 25. Evaluate Gradient Boosting Model
# ------------------------------------------------------------

gradient_boosting_accuracy = accuracy_score(
    y_test,
    gradient_boosting_predictions
)

gradient_boosting_precision = precision_score(
    y_test,
    gradient_boosting_predictions,
    pos_label="Placed"
)

gradient_boosting_recall = recall_score(
    y_test,
    gradient_boosting_predictions,
    pos_label="Placed"
)

gradient_boosting_f1 = f1_score(
    y_test,
    gradient_boosting_predictions,
    pos_label="Placed"
)


print("\n" + "=" * 60)
print("GRADIENT BOOSTING MODEL EVALUATION")
print("=" * 60)

print(f"\nAccuracy:  {gradient_boosting_accuracy:.4f}")
print(f"Precision: {gradient_boosting_precision:.4f}")
print(f"Recall:    {gradient_boosting_recall:.4f}")
print(f"F1 Score:  {gradient_boosting_f1:.4f}")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        gradient_boosting_predictions
    )
)


gradient_boosting_confusion_matrix = confusion_matrix(
    y_test,
    gradient_boosting_predictions,
    labels=[
        "Not Placed",
        "Placed"
    ]
)


print("\nConfusion Matrix:")

print(gradient_boosting_confusion_matrix)


# ------------------------------------------------------------
# 26. Create Baseline Model Comparison Table
# ------------------------------------------------------------

model_comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting"
    ],

    "Accuracy": [
        logistic_accuracy,
        decision_tree_accuracy,
        random_forest_accuracy,
        gradient_boosting_accuracy
    ],

    "Precision": [
        logistic_precision,
        decision_tree_precision,
        random_forest_precision,
        gradient_boosting_precision
    ],

    "Recall": [
        logistic_recall,
        decision_tree_recall,
        random_forest_recall,
        gradient_boosting_recall
    ],

    "F1 Score": [
        logistic_f1,
        decision_tree_f1,
        random_forest_f1,
        gradient_boosting_f1
    ]
})


# ------------------------------------------------------------
# Sort Models by F1 Score
# ------------------------------------------------------------

model_comparison = (
    model_comparison
    .sort_values(
        by="F1 Score",
        ascending=False
    )
    .reset_index(drop=True)
)


# ------------------------------------------------------------
# Display Model Comparison
# ------------------------------------------------------------

print("\n" + "=" * 60)

print("BASELINE MODEL COMPARISON")

print("=" * 60)

print(
    model_comparison.round(4).to_string(index=False)
)


# ------------------------------------------------------------
# Display Current Best Baseline Model
# ------------------------------------------------------------

best_baseline_model = model_comparison.iloc[0]["Model"]

print(
    f"\nCurrent Best Baseline Model: "
    f"{best_baseline_model}"
)

print(
    "\nNote: Final model selection will be performed "
    "after cross-validation and further evaluation."
)


# ------------------------------------------------------------
# 27. Configure Stratified 5-Fold Cross-Validation
# ------------------------------------------------------------

stratified_cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


placed_f1_scorer = make_scorer(
    f1_score,
    pos_label="Placed"
)


# ------------------------------------------------------------
# 28. Define Models for Cross-Validation
# ------------------------------------------------------------

models_for_cv = {
    "Logistic Regression": logistic_pipeline,
    "Decision Tree": decision_tree_pipeline,
    "Random Forest": random_forest_pipeline,
    "Gradient Boosting": gradient_boosting_pipeline
}


cv_results = []


print("\n" + "=" * 60)
print("5-FOLD STRATIFIED CROSS-VALIDATION")
print("=" * 60)


# ------------------------------------------------------------
# 29. Perform Cross-Validation
# ------------------------------------------------------------

for model_name, model_pipeline in models_for_cv.items():

    print(f"\nEvaluating: {model_name}")

    cv_scores = cross_val_score(
        model_pipeline,
        X_train,
        y_train,
        cv=stratified_cv,
        scoring=placed_f1_scorer,
        n_jobs=-1
    )

    cv_results.append({
        "Model": model_name,
        "Mean CV F1 Score": cv_scores.mean(),
        "CV F1 Std": cv_scores.std()
    })

    print(f"Fold F1 Scores: {cv_scores.round(4)}")
    print(f"Mean CV F1 Score: {cv_scores.mean():.4f}")
    print(f"CV F1 Standard Deviation: {cv_scores.std():.4f}")


# ------------------------------------------------------------
# 30. Create Cross-Validation Comparison Table
# ------------------------------------------------------------

cv_comparison = pd.DataFrame(cv_results)

cv_comparison = (
    cv_comparison
    .sort_values(
        by="Mean CV F1 Score",
        ascending=False
    )
    .reset_index(drop=True)
)


print("\n" + "=" * 60)
print("CROSS-VALIDATION MODEL COMPARISON")
print("=" * 60)

print(
    cv_comparison
    .round(4)
    .to_string(index=False)
)


best_cv_model = cv_comparison.iloc[0]["Model"]

print(
    f"\nBest Model Based on Mean CV F1 Score: "
    f"{best_cv_model}"
)



# ------------------------------------------------------------
# 31. Configure Logistic Regression Hyperparameter Grid
# ------------------------------------------------------------

logistic_param_grid = {
    "classifier__C": [
        0.01,
        0.1,
        1.0,
        10.0,
        100.0
    ],
    "classifier__class_weight": [
        None,
        "balanced"
    ]
}


# ------------------------------------------------------------
# 32. Create Grid Search
# ------------------------------------------------------------

logistic_grid_search = GridSearchCV(
    estimator=logistic_pipeline,
    param_grid=logistic_param_grid,
    scoring=placed_f1_scorer,
    cv=stratified_cv,
    n_jobs=-1,
    refit=True,
    return_train_score=True
)


print("\n" + "=" * 60)
print("LOGISTIC REGRESSION HYPERPARAMETER TUNING")
print("=" * 60)

print("\nStarting GridSearchCV...")


# ------------------------------------------------------------
# 33. Fit Grid Search on Training Data
# ------------------------------------------------------------

logistic_grid_search.fit(
    X_train,
    y_train
)


print("\nGridSearchCV completed successfully!")


# ------------------------------------------------------------
# 34. Display Best Results
# ------------------------------------------------------------

print("\nBest Hyperparameters:")

print(
    logistic_grid_search.best_params_
)


print("\nBest Cross-Validation F1 Score:")

print(
    round(
        logistic_grid_search.best_score_,
        4
    )
)


# ------------------------------------------------------------
# 35. Store Best Tuned Model
# ------------------------------------------------------------

best_logistic_model = (
    logistic_grid_search.best_estimator_
)


print(
    "\nBest tuned Logistic Regression model "
    "stored successfully!"
)


# ------------------------------------------------------------
# 36. Generate Predictions Using Tuned Logistic Regression
# ------------------------------------------------------------

tuned_logistic_predictions = best_logistic_model.predict(X_test)


# ------------------------------------------------------------
# 37. Evaluate Tuned Logistic Regression
# ------------------------------------------------------------

tuned_logistic_accuracy = accuracy_score(
    y_test,
    tuned_logistic_predictions
)

tuned_logistic_precision = precision_score(
    y_test,
    tuned_logistic_predictions,
    pos_label="Placed"
)

tuned_logistic_recall = recall_score(
    y_test,
    tuned_logistic_predictions,
    pos_label="Placed"
)

tuned_logistic_f1 = f1_score(
    y_test,
    tuned_logistic_predictions,
    pos_label="Placed"
)


print("\n" + "=" * 60)
print("TUNED LOGISTIC REGRESSION TEST EVALUATION")
print("=" * 60)

print(f"\nAccuracy:  {tuned_logistic_accuracy:.4f}")
print(f"Precision: {tuned_logistic_precision:.4f}")
print(f"Recall:    {tuned_logistic_recall:.4f}")
print(f"F1 Score:  {tuned_logistic_f1:.4f}")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        tuned_logistic_predictions
    )
)


tuned_logistic_confusion_matrix = confusion_matrix(
    y_test,
    tuned_logistic_predictions,
    labels=[
        "Not Placed",
        "Placed"
    ]
)


print("\nConfusion Matrix:")

print(tuned_logistic_confusion_matrix)


# ------------------------------------------------------------
# 38. Compare Original and Tuned Logistic Regression
# ------------------------------------------------------------

final_model_comparison = pd.DataFrame({
    "Model": [
        "Original Logistic Regression",
        "Tuned Logistic Regression"
    ],

    "Accuracy": [
        logistic_accuracy,
        tuned_logistic_accuracy
    ],

    "Precision": [
        logistic_precision,
        tuned_logistic_precision
    ],

    "Recall": [
        logistic_recall,
        tuned_logistic_recall
    ],

    "F1 Score": [
        logistic_f1,
        tuned_logistic_f1
    ]
})


print("\n" + "=" * 70)
print("ORIGINAL VS TUNED LOGISTIC REGRESSION")
print("=" * 70)

print(
    final_model_comparison
    .round(4)
    .to_string(index=False)
)


# ------------------------------------------------------------
# 39. Calculate Performance Improvement
# ------------------------------------------------------------

f1_improvement = (
    tuned_logistic_f1 - logistic_f1
)

recall_improvement = (
    tuned_logistic_recall - logistic_recall
)


print("\nPerformance Improvement:")

print(
    f"F1 Score Improvement: "
    f"{f1_improvement:.4f}"
)

print(
    f"Recall Improvement: "
    f"{recall_improvement:.4f}"
)


# ------------------------------------------------------------
# 40. Select Final Model
# ------------------------------------------------------------

final_model = best_logistic_model

print("\nFinal Selected Model: Tuned Logistic Regression")

print(
    "Reason: Best overall F1 score and improved recall "
    "for identifying placed students."
)


# ------------------------------------------------------------
# 41. Save Final Trained Model
# ------------------------------------------------------------

final_model_path = "models/final_placement_model.joblib"

joblib.dump(
    final_model,
    final_model_path
)

print("\n" + "=" * 60)
print("FINAL MODEL SAVED SUCCESSFULLY")
print("=" * 60)

print(f"\nModel saved to: {final_model_path}")