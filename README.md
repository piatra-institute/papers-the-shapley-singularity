# the-shapley-singularity

*The Shapley Singularity: Contribution, Intelligence, and the Compression of Economic Value.* When a firm grows after hiring, who made the growth? The question is a credit-assignment problem, and cooperative game theory solved its allocative core in 1953 with the Shapley value. This paper takes that solution seriously at the moment machine intelligence becomes a production factor. Three exact games carry the argument: a minimal firm where naive growth-per-head overstates the new hires more than fourfold and a three-way synergy belongs to no one; a task-continuum production game where total output multiplies sixfold while labor's share of attributed value collapses to an eighth, intelligence and its essential complements are forced to equal Shapley values by symmetry, and intelligence's share is capped at 1/(k+1) by k essential complements for any finite capability; and a verification pair locating the last human wage in certification and exhibiting the gap between contribution (the Shapley point) and appropriation (the core). The Shapley singularity is therefore an ownership event, not an intelligence event, and a Shapley value is an audit under a chosen value function, never a desert claim.

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build the-shapley-singularity`.

## Simulation

```bash
cd simulation
uv run run_all.py        # -> output/results.json and output/figures/*.png
```

Three exact, deterministic analyses in exact rational arithmetic (no seed). Every decimal in the paper's modelled sections is a key in `output/results.json`; the `papers claims` gate checks the prose against it. See `simulation/README.md`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
