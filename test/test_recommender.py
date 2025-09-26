import os
import json
import pytest
from backend.recommender import Recommender

DATA_PATH = "data/products.json"

@pytest.fixture(scope="module")
def recommender():
    # Ensure products.json exists
    assert os.path.exists(DATA_PATH), "Missing data/products.json"
    return Recommender(DATA_PATH)

def test_recommend_returns_list(recommender):
    results = recommender.recommend("analytics dashboard")
    assert isinstance(results, list)
    assert len(results) > 0
    assert "name" in results[0]  # ensure product structure

def test_recommend_relevant_result(recommender):
    results = recommender.recommend("task management")
    names = [p["name"].lower() for p in results]
    assert any("productivity" in n or "task" in n for n in names)

def test_empty_query(recommender):
    results = recommender.recommend("")
    assert isinstance(results, list)  # should not crash
    # either empty or still returns something
    assert results is not None

def test_invalid_query_type(recommender):
    with pytest.raises(Exception):
        recommender.recommend(None)
