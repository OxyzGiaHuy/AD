import pandas as pd

from scripts.hierarchical_bootstrap_comparison import hierarchical_bootstrap, paired_cells


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
