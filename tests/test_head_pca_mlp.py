import numpy as np

from src.models.head_pca import HeadPCA


def test_head_pca_mlp_api_scores_shapes_with_or_without_torch():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(2, 4, 8)).astype("float32")
    model = HeadPCA.fit(
        x,
        pca_components=2,
        alpha=0.5,
        seed=0,
        head_type="mlp",
        head_hidden_dim=8,
        train_steps=2,
        batch_size=8,
        device="cpu",
    )
    image_scores, patch_scores = model.score_images(x)
    assert image_scores.shape == (2,)
    assert patch_scores.shape == (2, 4)
    assert np.all((patch_scores >= 0.0) & (patch_scores <= 1.0))
