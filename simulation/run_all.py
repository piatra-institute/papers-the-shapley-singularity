"""Orchestrator: reproduces every number in the paper's modelled sections.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in
the modelled sections is a key in the JSON file. All three analyses are
deterministic (exact rational arithmetic throughout); there is no seed.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_attribution, plot_compression

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_attribution(results, str(OUT / "figures" / "attribution.png"))
    plot_compression(results, str(OUT / "figures" / "compression.png"))

    a, c, v = results["attribution"], results["compression"], results["verifier"]
    g = a["growth_shares"]
    print(f"attribution: growth 20 -> incumbents {g['incumbents']} | hires "
          f"{g['hires']} | demand {g['demand']}; per hire {a['per_hire_shapley']} "
          f"vs naive {a['per_hire_naive']}; three-way dividend "
          f"{a['harsanyi_dividends']['three_way']}")
    print(f"compression: crossover g*={c['crossover_g_main']} (alpha=6); "
          f"share_I at g=1: {c['psi_at_1']} -> ceiling "
          f"{c['ceiling_two_complements']}; labor share "
          f"{c['labor_share_start']} -> {c['labor_share_end']}")
    print(f"verifier: human-verification share_H={v['human_verification']['share_H']} "
          f"vs share_I={v['human_verification']['share_I']}; self-verification "
          f"share_H={v['self_verification']['share_H']} vs "
          f"share_I={v['self_verification']['share_I']} "
          f"(cliff {v['cliff_share']} of total, x{v['labor_drop_factor']})")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
