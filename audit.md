# Audit

Dated log of editorial passes and verification runs. Newest first. See the workspace docs (run `papers docs`): writing-pipeline.md §7 and refresh-pipeline.md.

## 2026-06-13 — voice reform

Scope: corpus-wide voice reform, applied to this paper as a reference exemplar. No change to the simulation, to any number, or to the citation set; the rework is structural and prose-level only.

Changes:

- Structure de-skeletoned: 10 numbered sections to 9. The bolt-on "Objections and Limits" (§9) was folded into the index section, now "An Index, and the Boundaries of the Audit" (§8), and its five "The first/second/third objection" openings were de-enumerated into flowing prose; the conclusion renumbered to §9. All §7 cross-references remain correct.
- Prose de-ticced against the new voice.md "second wave": removed the pet-vocabulary ("load-bearing sentences" and "load-bearing and invisible" in the close, "first-class entry" in §2), thinned the "exactly" density (advisory 22 to 16, keeping the uses where exact solution is the genuine methodological point), and cleared the one negate-pivot introduced during the merge.
- Every decimal and every citation preserved verbatim; both figures and their captions unchanged.

Verification:

- voice: 0 errors, 0 review-candidates.
- refs: 46 cited / 46 bib / 0 missing / 0 unused (unchanged).
- claims: 23 prose decimals, 0 without a matching results.json value (unchanged; numbers untouched).
- build: clean, both figures embedded, 0 missing-character warnings.
- check => PASS.

## 2026-06-10 — initial full build

Scope: first complete draft from the single seed chat. Wrote the simulation, the paper, and all provenance docs; brought the paper to a clean build.

Changes:

- simulation/: three exact, deterministic analyses (no seed, exact `fractions.Fraction` throughout). `attribution_game` (a three-player firm solved by full enumeration: naive growth-per-head vs Shapley vs the Harsanyi dividend ledger, plus Cohen's land/labour game and the symmetric complement pair). `compression_path` (a task-continuum production game over {I,C,E,H}; exact Shapley curves in the automatable share g and the AI productivity multiple alpha; the I=C=E symmetry, the crossover g*=3/alpha, the (4alpha-3)/12alpha share at g=1, and the 1/(k+1) ceiling, each asserted against its closed form before output). `verifier_and_power` (the two verification regimes at g=1, and the core geometry: Shapley point inside a wide or degenerate core). Two publication figures (attribution.png, compression.png). One-command run_all.py.
- paper/PAPER.md: 10 sections. The twenty units (§1); the failure of labor, capital, and marginal-product accounts on synergy (§2); the Shapley frame, causal v(S), and the ML rediscovery (§3); the firm recomputed with both figures' first panel (§4); intelligence as universal complement and the one-product conjecture (§5); the compression path, the symmetry, and the 1/(k+1) ceiling, with both figures embedded (§6); the verifier's wage and the Shapley-point-vs-core gap (§7); what an index would measure (§8); five objections (§9); the one-axis economy (§10). 46-entry bibliography.
- metadata.yaml: has_simulation true, claims_target results.json, abstract filled, date "June 2026", status built.
- brief.md, research.md (tiered, T1/T2 traced), sources.md (46 frozen entries), README.md, simulation/README.md.

Headline numbers (all keys in simulation/output/results.json):

- attribution: growth 20 splits incumbents 9.33 / hires 4.33 / demand 6.33; per-hire Shapley 0.43 vs naive 2.0 (overstatement 4.62x); Harsanyi dividends 6 (incumbents×hires) + 10 (incumbents×demand) + 4 (three-way) = 20; Cohen land 5.5 / labour 4.5; complement pair 50 / 50.
- compression (alpha=6): labor share 1.0 -> 0.125 while output multiplies sixfold; phi_I=phi_C=phi_E at every g; crossover g*=0.5; intelligence share at g=1 across alpha = 0.25 / 0.292 / 0.3125 / 0.328 for alpha = 3 / 6 / 12 / 48, ceiling 1/3; unanimity caps 1/(k+1) = 0.5 / 0.333 / 0.25 / 0.2 / 0.167 for k=1..5.
- verifier (g=1, alpha=6): human-verification labor share 0.375 (best-attributed) vs 0.208 per stack factor; self-verification labor 0.125 vs intelligence 0.292; cliff 1.5 units = 0.25 of total, a threefold drop. Core: labor floor share 0.167 with Shapley point 0.375; unanimity limit core is the whole simplex with Shapley point 0.333.

Verification:

- voice: 0 errors, 0 review-candidates (two negate-pivot/inline-contrastive warns in §3/§8 reworded away).
- refs: 46 cited / 46 bib / 0 missing / 0 unused.
- claims: 23 decimal claims, 0 without a matching simulation value (results.json carries 334 distinct numerics).
- build: 18 pages, both figures embedded (4 image XObjects), 0 missing-character warnings.
- check => PASS.

Notes / deferred:

- Tooling change: widened the refs-gate year pattern in `tooling/papers/commands/gates.py` from `(1[89]|20)\d{2}` to `(1[6-9]|20)\d{2}` so 18th/19th-century classics (Smith 1776, Ricardo 1817, Marx 1867, Wicksteed 1894, Clark 1899) are recognized as citations. This is a general improvement, not specific to this paper; the geodesics-of-care refs gate still passes 34/34 after the change.
- Both "von" authors written surname-first in the bibliography ("Neumann, J. von" / "Platz, J. von") so the gate's first-token surname match works, while prose cites "von Neumann" / "von Platz".
- Dropped from the seed: the sheaf-cohomology consistency thread, the neuron/edge attribution detour, and the fabricated "Shapley Singularity Index" numbers (the index survives as a described program in §8, never as computed values). The McKinsey EBIT figure was dropped as too volatile to freeze; the AI-Index investment figures motivate §5 in prose with no decimal claim.
- Status is `built`, not `published`: deploying to the web (sync + page.tsx) is the maintainer's pipeline.
