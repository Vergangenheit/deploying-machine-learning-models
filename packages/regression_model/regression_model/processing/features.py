import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

from regression_model.processing.errors import InvalidModelInputError


class LogTransformer(BaseEstimator, TransformerMixin):
    """Logarithm transformer."""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # to accomodate the pipeline
        return self

    def transform(self, X):
        X = X.copy()

        # check that the values are non-negative for log transform
        if not (X[self.variables] > 0).all().all():
            vars_ = self.variables[(X[self.variables] <= 0).any()]
            raise InvalidModelInputError(
                f"Variables contain zero or negative values, "
<<<<<<< HEAD
                f"can't apply log for vars: {vars_}"
            )
=======
                f"can't apply log for vars: {vars_}")
>>>>>>> 6162c318b58b225e0061fccd6c64cd67fe205c1b

        for feature in self.variables:
            X[feature] = np.log(X[feature])

        return X
