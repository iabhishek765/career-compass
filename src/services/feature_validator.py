import pandas as pd


def validate_student_features(student_df, expected_features):
    """
    Validate the student's input features.

    Parameters
    ----------
    student_df : pandas.DataFrame

    expected_features : list

    Returns
    -------
    pandas.DataFrame
    """

    expected_feature_set = set(expected_features)

    input_feature_set = set(student_df.columns)

    missing_features = expected_feature_set - input_feature_set

    extra_features = input_feature_set - expected_feature_set

    if missing_features:
        raise ValueError(
            f"Missing required features:\n"
            f"{sorted(missing_features)}"
        )

    if extra_features:
        raise ValueError(
            f"Unexpected extra features:\n"
            f"{sorted(extra_features)}"
        )

    student_df = student_df[list(expected_features)]

    return student_df