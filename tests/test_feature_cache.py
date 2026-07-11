from src.backbones.dinov2 import IdentityPatchBackbone
from src.data.datasets import synthetic_records
from src.run_experiment import encode_with_cache


def test_encode_with_cache_reuses_npz(tmp_path):
    records = synthetic_records("toy", count=4)
    backbone = IdentityPatchBackbone(feature_dim=4, patches=4)
    first = encode_with_cache(backbone, records, tmp_path, "toy", 0, "identity_patch", 64)
    cached = list(tmp_path.glob("*.npz"))
    assert len(cached) == 1
    second = encode_with_cache(backbone, records, tmp_path, "toy", 0, "identity_patch", 64)
    assert first.patch_features.shape == second.patch_features.shape
    assert first.grid_size == second.grid_size


def test_encode_with_cache_can_share_dinov2_eval_key_across_seeds(tmp_path):
    records = synthetic_records("toy", count=4)
    backbone = IdentityPatchBackbone(feature_dim=4, patches=4)
    first = encode_with_cache(backbone, records, tmp_path, "eval", 0, "dinov2_vits14", 64, cache_seed=0)
    second = encode_with_cache(backbone, records, tmp_path, "eval", 99, "dinov2_vits14", 64, cache_seed=0)
    cached = list(tmp_path.glob("*.npz"))
    assert len(cached) == 1
    assert first.patch_features.shape == second.patch_features.shape
