from services.model_loader import load_model

print("=" * 60)
print("MODEL LOADER TEST")
print("=" * 60)

model = load_model()

print(type(model))

print("\nModel loaded successfully.")