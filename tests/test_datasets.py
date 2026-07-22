import csv

import pytest

from src.data.datasets import ImageRecord, load_records
from src.data.sampling import few_shot_support


def _touch(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()


def test_mvtec_loader_preserves_split_label_and_mask(tmp_path):
    root = tmp_path / "mvtec"
    _touch(root / "bottle" / "train" / "good" / "001.png")
    _touch(root / "bottle" / "test" / "good" / "002.png")
    _touch(root / "bottle" / "test" / "broken" / "003.png")
    _touch(root / "bottle" / "ground_truth" / "broken" / "003_mask.png")

    records = load_records("mvtec", root, ["bottle"])

    assert [(record.split, record.label) for record in records] == [("train", 0), ("test", 1), ("test", 0)]
    anomaly = next(record for record in records if record.label == 1)
    assert anomaly.defect_type == "broken"
    assert anomaly.mask_path.endswith("003_mask.png")


def test_visa_csv_loader_resolves_paths_and_labels(tmp_path):
    root = tmp_path / "visa"
    image_paths = [
        "candle/Data/Images/Normal/train.png",
        "candle/Data/Images/Normal/test.png",
        "candle/Data/Images/Anomaly/bad.png",
    ]
    for image_path in image_paths:
        _touch(root / image_path)
    _touch(root / "candle/Data/Masks/Anomaly/bad.png")
    csv_path = root / "split_csv" / "1cls.csv"
    csv_path.parent.mkdir(parents=True)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["object", "split", "label", "image", "mask"])
        writer.writeheader()
        writer.writerow({"object": "candle", "split": "train", "label": "normal", "image": image_paths[0], "mask": ""})
        writer.writerow({"object": "candle", "split": "test", "label": "normal", "image": image_paths[1], "mask": ""})
        writer.writerow(
            {
                "object": "candle",
                "split": "test",
                "label": "anomaly",
                "image": image_paths[2],
                "mask": "candle/Data/Masks/Anomaly/bad.png",
            }
        )

    records = load_records("visa", root, "candle")

    assert len(records) == 3
    assert sum(record.split == "train" and record.label == 0 for record in records) == 1
    anomaly = next(record for record in records if record.label == 1)
    assert anomaly.mask_path.endswith("candle/Data/Masks/Anomaly/bad.png")


def test_loader_fails_on_unknown_class(tmp_path):
    root = tmp_path / "mvtec"
    _touch(root / "bottle" / "train" / "good" / "001.png")
    with pytest.raises(ValueError, match="absent"):
        load_records("mvtec", root, ["cable"])


def test_mpdd_uses_leakage_safe_mvtec_like_layout(tmp_path):
    root = tmp_path / "mpdd"
    _touch(root / "bracket_black" / "train" / "good" / "001.png")
    _touch(root / "bracket_black" / "test" / "good" / "002.png")
    _touch(root / "bracket_black" / "test" / "bad" / "003.png")
    records = load_records("mpdd", root, ["bracket_black"])
    assert {(record.split, record.label) for record in records} == {("train", 0), ("test", 0), ("test", 1)}


def test_few_shot_support_is_nested_across_k_for_fixed_seed():
    records = [
        ImageRecord(path=f"/data/a/train/{index}.png", category="a", split="train", label=0)
        for index in range(12)
    ]
    supports = {
        k: {record.path for record in few_shot_support(records, k=k, seed=7)}
        for k in [1, 2, 4, 8]
    }
    assert supports[1] < supports[2] < supports[4] < supports[8]
    assert supports[4] == {record.path for record in few_shot_support(records, k=4, seed=7)}
