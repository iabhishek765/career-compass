import joblib


# ------------------------------------------------------------
# 1. Define Saved Model Path
# ------------------------------------------------------------

model_path = "models/final_placement_model.joblib"


# ------------------------------------------------------------
# 2. Load Saved Model
# ------------------------------------------------------------

print("\nLoading saved model...")

loaded_model = joblib.load(model_path)

print("Model loaded successfully!")


# ------------------------------------------------------------
# 3. Display Model Information
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SAVED MODEL VERIFICATION")
print("=" * 60)

print(f"\nModel Type: {type(loaded_model)}")

print("\nPipeline Steps:")

for step_name, step_object in loaded_model.named_steps.items():
    print(f"{step_name}: {type(step_object).__name__}")


print("\n" + "=" * 60)
print("SAVED MODEL VERIFIED SUCCESSFULLY")
print("=" * 60)