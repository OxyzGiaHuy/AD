import numpy as np

from scripts.analyze_pvalue_uniformity import discrete_ks, monte_carlo_pvalue


def test_discrete_ks_zero_for_exact_uniform():
    k = 4
    grid = np.arange(1, k + 2) / (k + 1.0)
    p = np.repeat(grid, 20)
    d, nominal, empirical = discrete_ks(p, k)
    assert d < 1e-9
    assert np.allclose(nominal, empirical)


def test_discrete_ks_detects_anti_conservative_shift():
    k = 4
    p = np.full(100, 0.2)
    d, _, empirical = discrete_ks(p, k)
    assert d > 0.7
    assert empirical[0] == 1.0


def test_monte_carlo_pvalue_uniform_null_not_rejected():
    rng = np.random.default_rng(0)
    k = 4
    grid = np.arange(1, k + 2) / (k + 1.0)
    draws = rng.choice(grid, size=200)
    d, _, _ = discrete_ks(draws, k)
    mc_p = monte_carlo_pvalue(d, 200, k, iterations=500, rng=rng)
    assert mc_p > 0.05
