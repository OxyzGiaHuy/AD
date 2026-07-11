import numpy as np

from src.models.head_pca import CalibSubspaceHead, ShiftAwareCalibSubspaceHead


def test_calib_subspace_head_scores_and_features():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(3, 4, 8)).astype("float32")
    model = CalibSubspaceHead.fit(
        x,
        pca_components=2,
        seed=0,
        head_type="mlp",
        head_hidden_dim=8,
        train_steps=2,
        batch_size=8,
        device="cpu",
    )
    raw, patch = model.score_images(x)
    features = model.calibration_features(x)
    synth = model.synthetic_calibration_features(x, seed=1)
    assert raw.shape == (3,)
    assert patch.shape == (3, 4)
    assert features.shape == (3, 3)
    assert synth.shape[1] == 3
    assert model.storage_bytes() > 0



def test_shift_aware_calib_subspace_head_extends_calibration_only():
    rng = np.random.default_rng(1)
    x = rng.normal(size=(4, 5, 8)).astype("float32")
    base = CalibSubspaceHead.fit(
        x,
        pca_components=2,
        seed=1,
        head_type="mlp",
        head_hidden_dim=8,
        train_steps=2,
        batch_size=8,
        device="cpu",
    )
    shifted = ShiftAwareCalibSubspaceHead.fit(
        x,
        pca_components=2,
        seed=1,
        head_type="mlp",
        head_hidden_dim=8,
        train_steps=2,
        batch_size=8,
        device="cpu",
    )
    raw_base, patch_base = base.score_images(x)
    raw_shift, patch_shift = shifted.score_images(x)
    features = shifted.calibration_features(x)
    synth = shifted.synthetic_calibration_features(x, seed=2)
    assert raw_shift.shape == raw_base.shape == (4,)
    assert patch_shift.shape == patch_base.shape == (4, 5)
    assert features.shape == (4, 8)
    assert synth.shape[1] == 8
    assert shifted.storage_bytes() > base.storage_bytes()
