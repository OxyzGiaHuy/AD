from src.data.datasets import ImageRecord
from scripts.evaluate_corruptions import stratified_sample_records


def _records():
    return [
        ImageRecord(f"normal_{idx}.png", 0, "test", "toy") for idx in range(20)
    ] + [
        ImageRecord(f"anomaly_{idx}.png", 1, "test", "toy", "defect") for idx in range(20)
    ]


def test_stratified_sampling_is_balanced_and_deterministic():
    first = stratified_sample_records(_records(), max_images=10, seed=7)
    second = stratified_sample_records(_records(), max_images=10, seed=7)
    assert [record.path for record in first] == [record.path for record in second]
    assert sum(record.label == 0 for record in first) == 5
    assert sum(record.label == 1 for record in first) == 5


def test_stratified_sampling_changes_with_seed():
    first = stratified_sample_records(_records(), max_images=10, seed=7)
    second = stratified_sample_records(_records(), max_images=10, seed=8)
    assert [record.path for record in first] != [record.path for record in second]
