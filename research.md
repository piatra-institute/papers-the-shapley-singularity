# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2. T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only). A claim that reaches the paper rests on a T1 or T2 source.

Origin: one seed chat in `chats/` (a ChatGPT ideation thread that moved from "Marxist credit allocation" through Shapley values, neuron attribution, the analytical-Marxist precedents, and the pre-singularity intelligence economy to the title and a proposed structure). The chat is a lead only; every claim below was traced to a primary or authoritative source and frozen in `sources.md`. The chat's empirical citations (Stanford AI Index, McKinsey) were re-grounded; its mathematical claims (Shapley axioms, the I=C=E symmetry, the 1/(k+1) ceiling) were all re-derived exactly in the simulation rather than taken on the chat's word.

## Findings

### The formal core

- [T1] The Shapley value: the unique allocation satisfying efficiency, symmetry, the dummy axiom, and additivity, equal to the average marginal contribution over all orderings — Shapley (1953), *Contributions to the Theory of Games II*. The spine of the whole paper; re-derived by full enumeration in `analyses.py`.
- [T1] Marginality axiomatization: if a value depends only on a player's own marginal contributions, then symmetry + efficiency force the Shapley value — Young (1988), in *The Shapley Value*. Supports §3 and the objection-reply in §9 (Young prices the alternatives to averaging).
- [T1] Harsanyi dividends: the unique Möbius decomposition of a game into interaction terms; the Shapley value splits each dividend equally among its members — Harsanyi (1963), *Int. Econ. Rev.* 4:194. Supports §3-§4's synergy ledger; re-derived exactly.
- [T1] The characteristic function and the theory of cooperative games — von Neumann & Morgenstern (1944). Supplies the object $(N,v)$.
- [T1] The core: allocations no coalition can improve on by seceding — Gillies (1959). Supports §7's point-vs-zone result (Shapley point inside a wide or degenerate core).

### Classical political economy and the synergy it could not divide

- [T1] The division of labor in the pin factory: output multiplied by arrangement, not by any worker's separable contribution — Smith (1776), *Wealth of Nations* I.1. §2's opening; the celebration of synergy without an instrument to divide it.
- [T1] Distribution among classes as "the principal problem of political economy" — Ricardo (1817), *Principles*, Preface. §2.
- [T1] Surplus value as labor beyond the reproduction cost of labor power, appropriated through ownership; a class relation, not a metering of individual contribution — Marx (1867), *Capital* I. §2.
- [T1] Each factor paid its marginal product as natural law and moral desert — Clark (1899), *The Distribution of Wealth*. §2, the marginalist claim.
- [T1] Product exhaustion by marginal products holds exactly only under constant returns (Euler's theorem) — Wicksteed (1894), *Co-ordination of the Laws of Distribution*. §2's adding-up problem, the precise failure point.
- [T1] Team production: joint output is not a sum of separable individual outputs; metering individual contribution is the firm's defining difficulty — Alchian & Demsetz (1972), *Am. Econ. Rev.* 62:777. §2.
- [T1] Moral hazard in teams: no budget-balancing sharing rule makes every member internalize their full marginal effect — Holmström (1982), *Bell J. Econ.* 13:324. §2, the impossibility hardening.
- [T2] The economics of modern manufacturing as supermodular systems: returns to each activity rise with every other — Milgrom & Roberts (1990), *Am. Econ. Rev.* 80:511. §2, complementarity as the norm rather than the corner case.

### Cooperative game theory meets (and is refused by) political economy

- [T1] Exploitation rebuilt on coalitional counterfactuals: a group is exploited if it would do better withdrawing with its per-capita asset share — Roemer (1982), *A General Theory of Exploitation and Class*. §2, the closest approach inside Marxism.
- [T1] Cohen's land/labour Shapley example: land yields 1 alone, labour 0 alone, 10 together; Shapley gives land 5.5, labour 4.5 — Cohen (1995), *Self-Ownership, Freedom, and Equality*. §2 and §4 (re-derived exactly); the arithmetic embarrassment for the labor theory.
- [T2] The Shapley value considered as the repair for the adding-up problem and rejected on desert grounds (why the average over hypothetical orderings rather than the actual contribution?) — Reiff (2013), *Exploitation and Economic Justice*. §2 and the lead objection in §9.
- [T2] Meritocratic-capitalism dilemma: no notion of contribution both fits the actual capital-labour split and is morally plausible; references Shapley, Roth, Young — von Platz (2021), *Economics and Philosophy*. §2.
- [T2] Analytical Marxism and its game-theoretic turn — Elster (1985), *Making Sense of Marx*. §2's framing.
- [T2] The internal rejection: rational-choice Marxism as "static, ahistorical individualism" — Wood (1989), *New Left Review* I/177. §2, why no "Shapleyans" formed.

### Credit assignment in machine learning (the engineering rediscovery)

- [T1] Credit assignment named at the founding of AI — Minsky (1961), *Proc. IRE* 49:8. §1.
- [T2] RL as centrally the problem of distributing credit for success among many decisions — Sutton & Barto (2018), *Reinforcement Learning* (2nd ed.). §1.
- [T1] Difference rewards: score agent i by G(z) − G(z₋ᵢ), a marginal contribution to a coalition — Wolpert & Tumer (2001), *Adv. Complex Syst.* 4:265. §3, the Shapley integrand derived from engineering need.
- [T1] Counterfactual multi-agent policy gradients (COMA): a centralized critic marginalizes out one agent's action — Foerster, Farquhar, Afouras, Nardelli & Whiteson (2018), AAAI. §3.
- [T1] SHAP: a unified, game-theoretic feature-attribution framework; industrialized Shapley — Lundberg & Lee (2017), NeurIPS 30. §3.
- [T1] Causal Shapley values: attribution without causal structure misleads exactly as confounding does — Heskes, Sijben, Bucur & Claassen (2020), NeurIPS 33. §3's causal discipline.
- [T2] Superposition / polysemanticity: networks represent more features than neurons; the unit of contribution is itself unsettled — Elhage et al. (2022), *Transformer Circuits Thread*. §9's "player problem."

### AI, growth, automation, the singularity

- [T1] AI and economic growth: separating goods production from ideas production; AI in the ideas function is where singularities live; the binding constraint migrates to the hard-to-improve essential sector — Aghion, Jones & Jones (2019), in *The Economics of AI: An Agenda*. §5, §6, §9.
- [T1] Automation and new tasks: technology displaces labor from tasks and is reinstated by new tasks; the boundary is the moving frontier of automation — Acemoglu & Restrepo (2019), *J. Econ. Perspect.* 33:3. §5-§6, the parameter g.
- [T2] General purpose technologies as upstream "engines of growth" that reprice downstream activity, with long complementarity lags — Bresnahan & Trajtenberg (1995), *J. Econometrics* 65:83. §5.
- [T1] The productivity J-curve: GPT contributions are real, intangible, and invisible to output statistics during build-out — Brynjolfsson, Rock & Syverson (2021), *AEJ: Macro* 13:333. §5.
- [T1] AI and income distribution: the transition's distributional outcome turns on shares rather than absolutes; possible immiseration amid growth — Korinek & Stiglitz (2019), in *The Economics of AI: An Agenda*. §6.
- [T1] Economic-singularity tests: growth-acceleration evidence still says "not yet"; the brakes are real — Nordhaus (2021), *AEJ: Macro* 13:299. §6, §9.
- [T1] GPTs are GPTs: large-model task exposure concentrates in cognitive, educated, white-collar work — Eloundou, Manning, Mishkin & Rock (2024), *Science* 384:1306. §5, §8.
- [T1] AlphaFold: a fifty-year research bottleneck absorbed into a tool — Jumper, Evans, Pritzel, Green, Figurnov et al. (2021), *Nature* 596:583. §5, AI inside discovery.
- [T3] Macro motivation: hundreds of billions in annual corporate AI investment, majority firm adoption — Maslej, Fattorini, Perrault, Gil, Parli et al. (2025), *AI Index 2025*. §5, the input side (used for orientation only; no prose decimal depends on it).

### Bounds, limits, and the value-function problem

- [T1] Causal inference and the do-operator: v(S) is interventional, not observational — Pearl (2009), *Causality* (2nd ed.). §3.
- [T1] Goodhart's law in its original monetary habitat: a statistical regularity collapses once used for control — Goodhart (1975). §8.
- [T2] Audit-culture generalization: when a measure becomes a target it ceases to be a good measure — Strathern (1997), *European Review* 5:305. §8.
- [T1] Unbalanced growth / cost disease: value concentrates in sectors resistant to productivity gains — Baumol (1967), *Am. Econ. Rev.* 57:415. §9.
- [T1] Prices aggregate dispersed knowledge, but knowledge of scarcity and want, never of contribution — Hayek (1945), *Am. Econ. Rev.* 35:519. §7, why the market cannot answer the attribution question.
- [T1] National income is not a measure of welfare; the architect's own warning — Kuznets (1934), *National Income 1929–1932*. §8, against reading GDP for this question.
- [T2] Luck booked as skill: the meritocratic habit the demand-wave dividend names — Frank (2016), *Success and Luck*. §4.
- [T1] Tacit knowledge: we know more than we can tell; certification rests on it — Polanyi (1966), *The Tacit Dimension*. §7, why the verifier's wage may persist.
- [T1] Power indices as Shapley values; the value as civic infrastructure — Shapley & Shubik (1954), *Am. Polit. Sci. Rev.* 48:787; Shubik (1962), *Manag. Sci.* 8:325; Gale & Shapley (1962), *Am. Math. Monthly* 69:9. §2, "Shapley became plumbing."

## What was deliberately left out

- The chat's sheaf-cohomology thread (local-to-global consistency of attribution claims, coboundary obstructions) is genuinely interesting and entirely out of scope; the formal core stays cooperative game theory. Noted here as a possible sequel, not gestured at in the paper.
- The chat's "Shapley Singularity Index" was kept as a *described* measurement program in §8, not fabricated into numbers: no SSI value is computed or quoted, because none could be honestly grounded. The simulation's decimals are all exact game-theoretic facts, never empirical estimates.
- The neuron-attribution sub-thread (Neuron Shapley, edge/path attribution) survives only as the §9 "player problem" via the superposition citation; the paper does not detour into interpretability.
- No empirical share of intelligence in the real economy is asserted. The Maslej / AI-Index investment figures motivate §5 in prose without a decimal claim; the McKinsey EBIT figure from the chat was dropped as too volatile to freeze.
- The seed's framing flourishes ("rotato," "one product game") are reduced to their analytic content (the one-product conjecture and its correction to a one-axis economy).
