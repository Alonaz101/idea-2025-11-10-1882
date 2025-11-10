# Simple stub for ML-based recommendation engine

def ml_recommendation(mood, user_profile):
    # Dummy: enhance with real model
    base_recommendations = {
        "happy": [1],
        "relaxed": [2],
        "party": [1],
    }
    recs = base_recommendations.get(mood, [])
    # Simple personalization
    if user_profile.get('diet') == 'vegetarian':
        # remove recipes containing eggs (assumed non-vegetarian simple logic)
        recs = [rid for rid in recs if rid != 1]  # Assume recipe 1 not vegetarian
    return recs
