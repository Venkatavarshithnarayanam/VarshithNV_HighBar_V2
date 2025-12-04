import pandas as pd
import yaml
import os
from datetime import datetime

class DataLoader:

    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.expected_schema = self.config["schema"]
        self.dataset_path = self.config["dataset_path"]

    def validate_schema(self, df: pd.DataFrame):
        missing = [col for col in self.expected_schema.keys() if col not in df.columns]
        extra = [col for col in df.columns if col not in self.expected_schema.keys()]

        if missing:
            raise ValueError(f"Schema validation failed: Missing columns: {missing}")

        if extra:
            print(f"⚠ Warning: Unexpected columns detected: {extra} (Schema drift)")

    def drift_detection(self, df: pd.DataFrame):
        drift_cols = []
        for col, dtype in self.expected_schema.items():
            if dtype == int and not pd.api.types.is_integer_dtype(df[col]):
                drift_cols.append(col)
            if dtype == float and not pd.api.types.is_float_dtype(df[col]):
                drift_cols.append(col)
            if dtype == str and not pd.api.types.is_string_dtype(df[col]):
                drift_cols.append(col)

        if drift_cols:
            print(f"⚠ Data drift detected in columns: {drift_cols}")
        return drift_cols

    def load(self):
        try:
            df = pd.read_csv(self.dataset_path)
            df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

            self.validate_schema(df)
            drift = self.drift_detection(df)

            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "rows_loaded": len(df),
                "schema_status": "valid",
                "drift_columns": drift
            }

            os.makedirs("logs", exist_ok=True)
            with open(f"logs/data_loader_log.json", "w") as f:
                f.write(str(log_entry))

            return df

        except Exception as e:
            error_log = {
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "stage": "Data Loading"
            }
            with open(f"logs/data_loader_error_log.json", "w") as f:
                f.write(str(error_log))
            raise e
