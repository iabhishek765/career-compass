import joblib
from pathlib import Path


# ------------------------------------------------------------
# Model Path
# ------------------------------------------------------------

MODEL_PATH = Path("models/final_placement_model.joblib")


# ------------------------------------------------------------
# Load Model
# ------------------------------------------------------------

def load_model():
    """
    Load the trained Career Compass model.

    Returns
    -------
    sklearn model
    """

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at:\n{MODEL_PATH}"
        )

    model = joblib.load(MODEL_PATH)

    return model