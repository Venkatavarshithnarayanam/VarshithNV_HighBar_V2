import json
import os
from datetime import datetime

class CreativeEngine:

    def generate(self, evaluated_insights):

        creatives = []

        for item in evaluated_insights:
            roas_delta = item["evidence"]["roas_delta_pct"]
            ctr_delta = item["evidence"]["ctr_delta_pct"]

            if roas_delta < 0:
                idea = f"Introduce limited-time discount or bundle offer for {item['segment']} audience."
            elif ctr_delta < 0:
                idea = f"Test new visuals or headlines tailored to {item['segment']} to improve ad engagement."
            elif roas_delta > 10:
                idea = f"Scale winning offer by doubling daily budget for {item['segment']} audience."
            else:
                idea = f"Retain strategy but experiment with copy variations for {item['segment']}."

            creatives.append({
                "segment": item["segment"],
                "impact": item["impact"],
                "confidence": item["confidence"],
                "creative_idea": idea
            })

        os.makedirs("logs", exist_ok=True)
        with open(f"logs/creative_engine_log.json", "w") as f:
            f.write(json.dumps(creatives, indent=4))

        return creatives
