# Simulation — The Shapley Singularity

Three exact, deterministic analyses behind §4, §6, and §7 of the paper. No random seed: every Shapley value is computed by full enumeration of orderings in exact rational arithmetic (`fractions.Fraction`), every Harsanyi dividend by exact Möbius inversion, and every closed form quoted in the paper is asserted against the enumeration before anything is written out.

```bash
cd simulation
uv run run_all.py      # writes output/results.json and output/figures/*.png
```

Every decimal cited in the modelled sections is a key in `output/results.json` (the `papers claims` gate checks the paper's prose decimals against it).

## What it computes

`analyses.py`

- **`attribution_game`** — the firm puzzle (100 units, ten hires, 120 after) as a three-player game over the incumbent organization O, the hires N, and the demand wave M. Solved exactly: the naive growth-per-head rule (2.0 per hire) against the Shapley division (incumbents 9.33, hires 4.33, demand 6.33; 0.43 per hire, a 4.62× overstatement), and the Harsanyi dividend ledger that locates the twenty units as 6 (O×N) + 10 (O×M) + 4 (three-way) and shows the four-unit three-way synergy belongs to no factor alone. Includes Cohen's land/labour game (5.5 / 4.5) and the symmetric complement pair (50 / 50) as boundary calibrations.
- **`compression_path`** — a unit continuum of tasks, an automatable share g, four factors {intelligence I, compute C, energy E, human labor H}. The machine stack does automatable tasks at productivity α, humans do any task at 1, each task goes to the best producer present. Exact Shapley curves in g and α, each verified against its closed form: `φ_H = 1 − g/4`, `φ_I = φ_C = φ_E = g(4α−3)/12`, `v(N) = 1 + (α−1)g`. Yields the I=C=E symmetry at every point, the crossover g* = 3/α (0.5 at α=6), the labor-share collapse 1.0 → 0.125 with output multiplying sixfold, intelligence's share at g=1 of (4α−3)/12α (0.25 / 0.292 / 0.3125 / 0.328 for α = 3/6/12/48), and the 1/(k+1) ceiling computed from the unanimity game for k = 1..5 (0.5 / 0.333 / 0.25 / 0.2 / 0.167).
- **`verifier_and_power`** — two regimes at g=1, α=6. Human verification (machine output counts only when a human certifies it) makes labor the single best-attributed factor: share 0.375 against 0.208 per stack factor. Self-verification (the stack certifies itself) drops labor to 0.125 while intelligence rises to 0.292: a cliff of 1.5 units, a quarter of total value, a threefold fall in one step. Then the core: in the human-verification game labor's core floor is its outside option (share 0.167) while the Shapley point sits at 0.375; in the displacement limit the game is unanimity on {I,C,E} and the core is the whole simplex while the Shapley point is 1/3 each. Contribution determinate, appropriation indeterminate.

`figures.py` (pure plotters, read the results dict)

- `output/figures/attribution.png` — the twenty units, naive vs Shapley, beside the Harsanyi ledger that isolates the three-way synergy.
- `output/figures/compression.png` — Shapley shares along g at α=6 with the crossover; intelligence's share against g across the α family beneath the one-third ceiling; the verification cliff at g=1.

## Status

Complete and minimal. The model is a fact about itself: it shows the structural features claimed for attribution under complementarity (the synergy residue, the forced symmetry of essential complements, the 1/(k+1) ceiling, the point-vs-core gap) are realizable and exact, not that any empirical firm or economy exhibits these particular magnitudes ("calibration is not fitting"). The decimals are exact game-theoretic facts about exactly specified games; what transfers to the world is their shape (the asymmetries, the ceiling, the orderings), not the numbers. Dependencies: `matplotlib` only (see `pyproject.toml`).
