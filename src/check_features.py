from services.model_loader import load_model

model = load_model()

print("\nModel Features:\n")

for feature in model.feature_names_in_:
    print(feature)