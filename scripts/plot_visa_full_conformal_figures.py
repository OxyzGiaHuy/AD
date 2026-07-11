from __future__ import annotations

import csv
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def read_csv(path: Path) -> list[dict]:
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main() -> int:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    out_dir = Path('outputs/figures')
    out_dir.mkdir(parents=True, exist_ok=True)
    bins = read_csv(Path('outputs/paper_tables/visa_full_conformal_reliability_bins.csv'))
    summary = read_csv(Path('outputs/paper_tables/visa_full_conformal_vs_baselines_k_corruption.csv'))

    # Reliability diagrams for LOIO all, k=4, k=8.
    for k_label, title, suffix in [(None, 'Full VisA LOIO reliability', 'all'), ('4', 'Full VisA LOIO reliability, k=4', 'k4'), ('8', 'Full VisA LOIO reliability, k=8', 'k8')]:
        rows = [r for r in bins if r.get('prob_col') == 'conformal_prob_loio']
        if k_label is None:
            rows = [r for r in rows if 'k_shot' not in r or r.get('k_shot','') == ''][:15]
        else:
            rows = [r for r in rows if r.get('k_shot') == k_label]
        rows = sorted(rows, key=lambda r: int(r['bin']))
        conf = [float(r['confidence']) if r['confidence'] != 'nan' else np.nan for r in rows]
        acc = [float(r['accuracy']) if r['accuracy'] != 'nan' else np.nan for r in rows]
        n = [int(r['n']) for r in rows]
        x = np.arange(len(rows))
        plt.figure(figsize=(6.2, 4.6))
        plt.plot([0, len(rows)-1], [0, 1], color='0.7', linestyle='--', label='ideal')
        plt.plot(x, conf, marker='o', label='confidence')
        plt.plot(x, acc, marker='s', label='empirical anomaly rate')
        plt.bar(x, np.asarray(n) / max(sum(n), 1), alpha=0.18, label='bin mass')
        plt.ylim(0, 1)
        plt.xlabel('Probability bin')
        plt.ylabel('Value')
        plt.title(title)
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(out_dir / f'visa_full_loio_reliability_{suffix}.png', dpi=200)
        plt.close()

    # ECE by corruption comparing methods.
    methods = ['vector_platt', 'shift_aware_vector_platt', 'conformal_prob_loio', 'conformal_prob_weighted']
    method_labels = ['Vector', 'Shift-aware', 'LOIO conformal', 'Weighted conformal']
    for k in ['4', '8']:
        corrs = ['blur', 'brightness_contrast', 'gaussian_noise', 'jpeg']
        values = []
        for method in methods:
            vals = []
            for corr in corrs:
                match = [r for r in summary if r['group_type']=='k_corruption' and r['key0']==k and r['key1']==corr and r['prob_col']==method]
                vals.append(float(match[0]['ece']) if match else np.nan)
            values.append(vals)
        x = np.arange(len(corrs))
        width = 0.18
        plt.figure(figsize=(8.2, 4.8))
        for i, vals in enumerate(values):
            plt.bar(x + (i - 1.5) * width, vals, width, label=method_labels[i])
        plt.xticks(x, ['blur', 'brightness', 'gaussian', 'jpeg'])
        plt.ylabel('ECE')
        plt.title(f'Full VisA calibration under corruption, k={k}')
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(out_dir / f'visa_full_ece_by_corruption_k{k}.png', dpi=200)
        plt.close()

    manifest = Path('outputs/figures/visa_full_conformal_figure_manifest.md')
    manifest.write_text('\n'.join([
        '# Full VisA Conformal Figure Manifest',
        '',
        '- `visa_full_loio_reliability_all.png`: reliability diagram for LOIO conformal on all k4/k8 VisA corruptions.',
        '- `visa_full_loio_reliability_k4.png`: reliability diagram for LOIO conformal at k=4.',
        '- `visa_full_loio_reliability_k8.png`: reliability diagram for LOIO conformal at k=8.',
        '- `visa_full_ece_by_corruption_k4.png`: ECE bar chart comparing Vector, Shift-aware, LOIO, and Weighted conformal at k=4.',
        '- `visa_full_ece_by_corruption_k8.png`: ECE bar chart comparing Vector, Shift-aware, LOIO, and Weighted conformal at k=8.',
    ]) + '\n', encoding='utf-8')
    print('wrote figures to outputs/figures')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
