from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

pipe = make_pipeline(
    SimpleImputer(strategy="median"),
    DecisionTreeClassifier(max_depth=5)
)

def get_estimator():
    return pipe
