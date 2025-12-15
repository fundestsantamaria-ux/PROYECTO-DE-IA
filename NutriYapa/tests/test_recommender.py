from src.recommender import NutriRecommender
import pandas as pd

def test_basic_recommendation():
    items = pd.DataFrame([
        {"calories":300,"protein":25},
        {"calories":700,"protein":10}
    ])
    user = {"goal":"gain_muscle"}

    r = NutriRecommender()
    recs = r.recommend_for_user(user, items, top_k=2)
    
    assert len(recs) == 2
