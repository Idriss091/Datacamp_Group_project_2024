import os
import pandas as pd
import rampwf as rw
from sklearn.model_selection import StratifiedShuffleSplit

# Problem title
problem_title = "Classification of Solar Energy Output"

# Target column for classification
_target_column_name = "DC_POWER_CATEGORY"
_ignore_column_names = ["DC_POWER", "AC_POWER", "TOTAL_YIELD"]
_prediction_label_names = [0, 1, 2, 3, 4, 5, 6]

# Define prediction type
Predictions = rw.prediction_types.make_multiclass(
    label_names=_prediction_label_names
)

# Define the workflow (simpler model initially)
workflow = rw.workflows.Estimator()

# Define scoring metric (Accuracy)
score_types = [
    rw.score_types.Accuracy(name="acc", precision=4),
]

# Cross-validation strategy
def get_cv(X, y):
    return StratifiedShuffleSplit(n_splits=8, test_size=0.2, random_state=42).split(X, y)

# Function to load data
def _read_data(path, filename):
    df = pd.read_csv(os.path.join(path, "data", filename))
    y_array = df[_target_column_name].values.astype(int)
    X_df = df.drop(columns=[_target_column_name] + _ignore_column_names, errors='ignore')
    return X_df, y_array

# Load train data
def get_train_data(path="."):
    return _read_data(path, "train.csv")

# Load test data
def get_test_data(path="."):
    return _read_data(path, "test.csv")