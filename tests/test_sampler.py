from src.data.datasets import synthetic_records
from src.data.sampling import evaluation_records, few_shot_support, split_calibration


def test_few_shot_sampler_is_deterministic_and_no_test_leak():
    records = synthetic_records("toy", count=12)
    a = few_shot_support(records, k=1, seed=7)
    b = few_shot_support(records, k=1, seed=7)
    assert a == b
    assert all(r.split == "train" and r.label == 0 for r in a)
    assert not set(a).intersection(evaluation_records(records))

def test_split_calibration_holds_out_anomaly_validation_without_eval_leak():
    records = synthetic_records("toy", count=24)
    calib_a, eval_a = split_calibration(records, seed=3, anomaly_fraction=0.25)
    calib_b, eval_b = split_calibration(records, seed=3, anomaly_fraction=0.25)
    assert calib_a == calib_b
    assert eval_a == eval_b
    assert calib_a
    assert all(r.split == "test" and r.label == 1 for r in calib_a)
    assert not set(calib_a).intersection(eval_a)
    assert all(r.split == "test" for r in eval_a)
    assert any(r.label == 0 for r in eval_a)
    assert any(r.label == 1 for r in eval_a)
