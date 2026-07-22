import pandas as pd

from scripts.hierarchical_bootstrap_comparison import compare, hierarchical_bootstrap, paired_cells


def test_hierarchical_bootstrap_recovers_constant_paired_delta():
    rows = []
    for cls in ["a", "b", "c"]:
        for seed in [0, 1]:
            rows.extend([
                {"dataset": "toy", "class": cls, "k_shot": 4, "seed": seed, "method": "base", "power": 0.2},
                {"dataset": "toy", "class": cls, "k_shot": 4, "seed": seed, "method": "new", "power": 0.3},
            ])
    cells = paired_cells(pd.DataFrame(rows), "base", "new", "power")
    result = hierarchical_bootstrap(cells, iterations=200, seed=3)
    assert abs(result["delta_mean"] - 0.1) < 1e-9
    assert abs(result["ci95_low"] - 0.1) < 1e-9
    assert abs(result["ci95_high"] - 0.1) < 1e-9


def test_bonferroni_intervals_are_not_narrower_than_pointwise_intervals():
    rows = []
    for cls_index, cls in enumerate(["a", "b", "c", "d"]):
        for seed in [0, 1, 2]:
            base = 0.1 * cls_index + 0.02 * seed
            rows.extend([
                {"dataset": "toy", "class": cls, "k_shot": 4, "seed": seed, "method": "base", "power": base, "false_alarm_rate": base / 2},
                {"dataset": "toy", "class": cls, "k_shot": 4, "seed": seed, "method": "new", "power": base + 0.03 * (cls_index + 1), "false_alarm_rate": base / 2 - 0.01 * seed},
            ])
    frame = pd.DataFrame(rows)
    adjusted = compare(frame, "base", ["new"], ["power", "false_alarm_rate"], 1000, 4)
    pointwise = compare(frame, "base", ["new"], ["power", "false_alarm_rate"], 1000, 4, multiplicity="pointwise")
    assert (adjusted["family_size"] == 2).all()
    assert (adjusted["ci_low"] <= pointwise["ci_low"]).all()
    assert (adjusted["ci_high"] >= pointwise["ci_high"]).all()
    assert (adjusted["ci_low"] <= adjusted["ci95_low"]).all()
    assert (adjusted["ci_high"] >= adjusted["ci95_high"]).all()
