from b2w_reviews.logs import log
## add pytest

@log
def test_reviewer_id_nunique(df):
    assert df["reviewer_id"].nunique() == df.shape[0]