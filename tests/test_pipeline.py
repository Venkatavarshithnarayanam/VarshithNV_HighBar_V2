from agents.data_loader import DataLoader
from agents.insight_engine import InsightEngine
from evaluator.evaluator import Evaluator

def test_schema_validation():
    loader = DataLoader()
    df = loader.load()
    assert df is not None

def test_insight_generation():
    loader = DataLoader()
    df = loader.load()
    engine = InsightEngine()
    insights = engine.build_insights(df)
    assert len(insights) >= 1

def test_evaluator_output():
    loader = DataLoader()
    df = loader.load()
    engine = InsightEngine()
    insights = engine.build_insights(df)
    evaluator = Evaluator()
    evaluated = evaluator.evaluate(insights)
    assert "confidence" in evaluated[0]
