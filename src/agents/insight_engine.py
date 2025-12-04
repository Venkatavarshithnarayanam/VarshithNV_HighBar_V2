import pandas as pd
import numpy as np
from datetime import datetime
import os

class InsightEngine:

    def __init__(self):
        self.segments = ["campaign_name"]  

    def compute_baseline(self, df):
        if "ctr" not in df.columns:
            df["ctr"] = (df["clicks"] / df["impressions"]).replace([np.inf], 0).fillna(0)

        if "roas" not in df.columns:
            df["roas"] = (df["revenue"] / df["spend"]).replace([np.inf], 0).fillna(0)

        return {
            "baseline_ctr": df["ctr"].mean(),
            "baseline_roas": df["roas"].mean()
        }

    def build_insights(self, df):
        baseline = self.compute_baseline(df)
        insights = []

        for segment in self.segments:
            grouped = df.groupby(segment).agg({
                "ctr": "mean",
                "roas": "mean",
                "impressions": "sum"
            }).reset_index()

            for _, row in grouped.iterrows():
                ctr_delta = ((row["ctr"] - baseline["baseline_ctr"]) / baseline["baseline_ctr"]) * 100 if baseline["baseline_ctr"] else 0
                roas_delta = ((row["roas"] - baseline["baseline_roas"]) / baseline["baseline_roas"]) * 100 if baseline["baseline_roas"] else 0

                insight = {
                    "segment_type": segment,
                    "segment": row[segment],
                    "ctr_delta_pct": round(ctr_delta, 2),
                    "roas_delta_pct": round(roas_delta, 2),
                    "ctr_current": round(row["ctr"], 4),
                    "ctr_baseline": round(baseline["baseline_ctr"], 4),
                    "roas_current": round(row["roas"], 4),
                    "roas_baseline": round(baseline["baseline_roas"], 4),
                }
                insights.append(insight)

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "insights_generated": len(insights),
            "baseline": baseline
        }

        os.makedirs("logs", exist_ok=True)
        with open("logs/insight_engine_log.json", "w") as f:
            f.write(str(log_entry))

        return insights
