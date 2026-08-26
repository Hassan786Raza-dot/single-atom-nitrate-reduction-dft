#!/usr/bin/python3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

src = Path('data/convergence/convergence.csv')
out = Path('figures/final/convergence_benchmark.png')
df = pd.read_csv(src)
fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), constrained_layout=True)
for ax, family in zip(axes, ['cutoff', 'kmesh', 'vacuum']):
    sub = df[df.family == family].copy()
    x = sub['cutoff_eV'] if family == 'cutoff' else sub['vacuum_A'] if family == 'vacuum' else range(len(sub))
    labels = sub['label'] if family == 'kmesh' else None
    ax.plot(list(x), sub['energy_eV'], marker='o')
    if labels is not None:
        ax.set_xticks(list(x), list(labels))
    ax.set_title(f'{family} sensitivity')
    ax.set_ylabel('Total energy (eV)')
    ax.grid(alpha=0.25)
fig.savefig(out, dpi=300)
print(out)
