import json
import pandas as pd
from agents.data_loader import DataLoader
from agents.insight_engine import InsightEngine
from evaluator.evaluator import Evaluator
from agents.creative_engine import CreativeEngine
from datetime import datetime
import os

def save_json(data, filename):
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/{filename}", "w") as f:
        json.dump(data, f, indent=4)

def run_pipeline():
    loader = DataLoader()
    df = loader.load()

    insight_engine = InsightEngine()
    insights = insight_engine.build_insights(df)

    evaluator = Evaluator()
    evaluated_insights = evaluator.evaluate(insights)

    creative_engine = CreativeEngine()
    creatives = creative_engine.generate(evaluated_insights)

    save_json(evaluated_insights, "insights.json")
    save_json(creatives, "creatives.json")

    metrics = {
        "total_insights": len(evaluated_insights),
        "segments_covered": list(set([i["segment"] for i in evaluated_insights])),
        "timestamp": datetime.now().isoformat()
    }
    save_json(metrics, "metrics.json")

if __name__ == "__main__":
    run_pipeline()
