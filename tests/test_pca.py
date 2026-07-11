import numpy as np

from src.models.pca import PCASubspace


def test_pca_residual_scores_shape():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(3, 4, 8)).astype("float32")
    pca = PCASubspace.fit(x, n_components=2)
    scores = pca.residual_scores(x)
    assert scores.shape == (3, 4)
    assert np.all(scores >= 0)

