from regression_model.config import config

import pandas as pd


def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for unprocessable values."""

    validated_data = input_data.copy()

    # check for numerical variables with NA not seen during training
    if input_data[config.NUMERICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
<<<<<<< HEAD
            axis=0, subset=config.NUMERICAL_NA_NOT_ALLOWED
        )
=======
            axis=0, subset=config.NUMERICAL_NA_NOT_ALLOWED)
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b

    # check for categorical variables with NA not seen during training
    if input_data[config.CATEGORICAL_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(
<<<<<<< HEAD
            axis=0, subset=config.CATEGORICAL_NA_NOT_ALLOWED
        )
=======
            axis=0, subset=config.CATEGORICAL_NA_NOT_ALLOWED)
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b

    # check for values <= 0 for the log transformed variables
    if (input_data[config.NUMERICALS_LOG_VARS] <= 0).any().any():
        vars_with_neg_values = config.NUMERICALS_LOG_VARS[
<<<<<<< HEAD
            (input_data[config.NUMERICALS_LOG_VARS] <= 0).any()
        ]
        validated_data = validated_data[validated_data[vars_with_neg_values] > 0]
=======
            (input_data[config.NUMERICALS_LOG_VARS] <= 0).any()]
        validated_data = validated_data[
            validated_data[vars_with_neg_values] > 0]
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b

    return validated_data
