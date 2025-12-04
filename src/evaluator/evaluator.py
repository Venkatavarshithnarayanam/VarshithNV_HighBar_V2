import math
import json
import os
from datetime import datetime
import yaml

class Evaluator:

    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.thresholds = self.config["thresholds"]

    def score_severity(self, delta):
        if abs(delta) >= self.thresholds["severity_high"]:
            return "high"
        elif abs(delta) >= self.thresholds["roas_drop_pct"]:
            return "medium"
        return "low"

    def confidence(self, ctr_delta, roas_delta, impressions):
        weight = self.thresholds["confidence_weight"]
        delta_strength = (abs(ctr_delta) + abs(roas_delta)) / 2
        logistic = 1 / (1 + math.exp(-weight * delta_strength))
        sample_factor = min(1, impressions / 5000) 
        return round((logistic + sample_factor) / 2, 2)

    def evaluate(self, insights):
        evaluated = []

        for insight in insights:
            severity = self.score_severity(insight["roas_delta_pct"])
            confidence_score = self.confidence(
                insight["ctr_delta_pct"],
                insight["roas_delta_pct"],
                insight.get("impressions", 0)
            )

            insight_eval = {
                "hypothesis": f"{insight['segment']} performance shift",
                "segment": insight["segment"],
                "impact": severity,
                "confidence": confidence_score,
                "evidence": {
                    "ctr_delta_pct": insight["ctr_delta_pct"],
                    "roas_delta_pct": insight["roas_delta_pct"],
                    "ctr_baseline": insight["ctr_baseline"],
                    "roas_baseline": insight["roas_baseline"]
                }
            }

            evaluated.append(insight_eval)

        os.makedirs("logs", exist_ok=True)
        with open(f"logs/evaluator_log.json", "w") as f:
            f.write(json.dumps(evaluated, indent=4))

        return evaluated
