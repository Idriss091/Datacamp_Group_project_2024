import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import kagglehub
import shutil

# File paths
DATA_DIR = "data"
PUBLIC_DIR = os.path.join(DATA_DIR, "public")
TRAIN_FILE = os.path.join(DATA_DIR, "train.csv")
TEST_FILE = os.path.join(DATA_DIR, "test.csv")
PUBLIC_TRAIN_FILE = os.path.join(PUBLIC_DIR, "train.csv")
PUBLIC_TEST_FILE = os.path.join(PUBLIC_DIR, "test.csv")

# Ensure directories exist
os.makedirs(PUBLIC_DIR, exist_ok=True)

def download_dataset():
    """Downloads the dataset from Kaggle and returns the path to the generation data CSV."""
    print("Downloading dataset...")
    dataset_path = kagglehub.dataset_download("anikannal/solar-power-generation-data")
    csv_path = os.path.join(dataset_path, "Plant_1_Generation_Data.csv")
    return csv_path

def load_and_clean_data(csv_path):
    print("Loading dataset...")
    df = pd.read_csv(csv_path)

    # Convert timestamp column
    if "DATE_TIME" in df.columns:
        df["DATE_TIME"] = pd.to_datetime(df["DATE_TIME"], format="%d-%m-%Y %H:%M")

    # Extract time-based features
    df["hour"] = df["DATE_TIME"].dt.hour
    df["day"] = df["DATE_TIME"].dt.day
    df["month"] = df["DATE_TIME"].dt.month

    # Drop original timestamp column
    df.drop(columns=["DATE_TIME"], inplace=True)

    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Encode categorical columns
    categorical_cols = ["SOURCE_KEY"]
    for col in categorical_cols:
        df[col] = df[col].astype("category").cat.codes  # Convert category to numerical

    # Create  power categories for classification
    bins = [-1, 10, 1500, 3500, 6000, 8000, 10000, np.inf]
    labels = ["Very Low", "Low", "Moderate", "Medium", "High", "Very High", "Extreme"]

    df["DC_POWER_CATEGORY"] = pd.cut(df["DC_POWER"], bins=bins, labels=labels)

    # Encode the classification target
    label_encoder = LabelEncoder()
    df["DC_POWER_CATEGORY"] = label_encoder.fit_transform(df["DC_POWER_CATEGORY"])

    print(" Column types after processing:")
    print(df.dtypes)

    return df

def split_and_save_data():
    # Download dataset and get CSV path
    csv_path = download_dataset()

    # Load and clean data
    df = load_and_clean_data(csv_path)

    # Remove downloaded files
    downloaded_dir = os.path.dirname(csv_path)
    shutil.rmtree(downloaded_dir)
    print(f"Cleaned up downloaded files from: {downloaded_dir}")

    # Split into private train/test
    print("Splitting data into private train & test sets...")
    df_train, df_test = train_test_split(
        df, test_size=0.2, random_state=42, stratify=df["DC_POWER_CATEGORY"]
    )
    print(f"Private Data: Train = {len(df_train)}, Test = {len(df_test)}")

    # Create public split from private train
    df_public_train, df_public_test = train_test_split(
        df_train, test_size=0.25, random_state=42, stratify=df_train["DC_POWER_CATEGORY"]
    )
    print(f"Public Data: Train = {len(df_public_train)}, Test = {len(df_public_test)}")

    # Save all datasets
    df_train.to_csv(TRAIN_FILE, index=False)
    df_test.to_csv(TEST_FILE, index=False)
    df_public_train.to_csv(PUBLIC_TRAIN_FILE, index=False)
    df_public_test.to_csv(PUBLIC_TEST_FILE, index=False)

if __name__ == "__main__":
    split_and_save_data()