# Sources

The frozen bibliography. Each entry in the form it takes in the paper's `## References`, with a one-line provenance note. See the workspace docs (`papers docs`): research-pipeline.md §4. Every in-text `et al.` maps to a co-authored entry here. 46 entries; `papers refs` reports 46 cited / 46 bib / 0 missing / 0 unused.

Two refs-gate notes. (1) The classics use 17xx–18xx years, so the gate's year pattern was widened from `(1[89]|20)\d{2}` to `(1[6-9]|20)\d{2}` in `tooling/papers/commands/gates.py` to recognize Smith (1776), Ricardo (1817), Marx (1867), Clark (1899), Wicksteed (1894). (2) The two "von" authors are written surname-first in the bibliography (`Neumann, J. von` and `Platz, J. von`) so the bib line's first token is the capitalized surname the gate keys on, while the prose cites "von Neumann and Morgenstern (1944)" and "von Platz (2021)" with the lowercase particle; the lead-surname resolves to `Neumann` / `Platz` by skipping the particle, matching the bib.

## Bibliography

Acemoglu, D., and Restrepo, P. (2019). Automation and new tasks: How technology displaces and reinstates labor. *Journal of Economic Perspectives*, 33(2), 3–30. — the task frontier; supplies the parameter g (§5-§6).

Aghion, P., Jones, B. F., and Jones, C. I. (2019). Artificial intelligence and economic growth. In A. Agrawal, J. Gans, and A. Goldfarb (Eds.), *The Economics of Artificial Intelligence: An Agenda* (pp. 237–282). University of Chicago Press. — ideas-production function; singularities; the migrating constraint (§5, §6, §9).

Alchian, A. A., and Demsetz, H. (1972). Production, information costs, and economic organization. *American Economic Review*, 62(5), 777–795. — team production; metering as the firm's defining difficulty (§2).

Baumol, W. J. (1967). Macroeconomics of unbalanced growth: The anatomy of urban crisis. *American Economic Review*, 57(3), 415–426. — cost disease; value concentrates in the unautomated (§9).

Bresnahan, T. F., and Trajtenberg, M. (1995). General purpose technologies: 'Engines of growth'? *Journal of Econometrics*, 65(1), 83–108. — GPTs reprice downstream activity, with lags (§5).

Brynjolfsson, E., Rock, D., and Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics*, 13(1), 333–372. — the accounting shadow of complementarity lags (§5).

Clark, J. B. (1899). *The Distribution of Wealth: A Theory of Wages, Interest and Profits*. Macmillan. — marginal product as natural law and desert (§2).

Cohen, G. A. (1995). *Self-Ownership, Freedom, and Equality*. Cambridge University Press. — the land/labour Shapley example, re-derived exactly (§2, §4).

Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., et al. (2022). Toy models of superposition. *Transformer Circuits Thread*. Anthropic. — polysemanticity; the unit-of-contribution fog inside the bloc (§9).

Eloundou, T., Manning, S., Mishkin, P., and Rock, D. (2024). GPTs are GPTs: Labor market impact potential of large language models. *Science*, 384(6702), 1306–1308. — exposure concentrated in white-collar cognitive work (§5, §8).

Elster, J. (1985). *Making Sense of Marx*. Cambridge University Press. — the analytical-Marxist program (§2).

Foerster, J., Farquhar, G., Afouras, T., Nardelli, N., and Whiteson, S. (2018). Counterfactual multi-agent policy gradients. In *Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence*. — COMA; the counterfactual critic (§3).

Frank, R. H. (2016). *Success and Luck: Good Fortune and the Myth of Meritocracy*. Princeton University Press. — luck booked as skill; the demand-wave dividend (§4).

Gale, D., and Shapley, L. S. (1962). College admissions and the stability of marriage. *American Mathematical Monthly*, 69(1), 9–15. — matching theory; the value as infrastructure (§2).

Gillies, D. B. (1959). Solutions to general non-zero-sum games. In A. W. Tucker and R. D. Luce (Eds.), *Contributions to the Theory of Games, Volume IV* (pp. 47–85). Princeton University Press. — the core; the point-vs-zone result (§7).

Goodhart, C. A. E. (1975). Problems of monetary management: The UK experience. In *Papers in Monetary Economics, Volume I*. Reserve Bank of Australia. — the law's original monetary statement (§8).

Harsanyi, J. C. (1963). A simplified bargaining model for the n-person cooperative game. *International Economic Review*, 4(2), 194–220. — dividends; the synergy ledger, re-derived exactly (§3, §4).

Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review*, 35(4), 519–530. — prices aggregate scarcity, not contribution (§7).

Heskes, T., Sijben, E., Bucur, I. G., and Claassen, T. (2020). Causal Shapley values: Exploiting causal knowledge to explain individual predictions of complex models. In *Advances in Neural Information Processing Systems 33*. — attribution without causal structure misleads (§3).

Holmström, B. (1982). Moral hazard in teams. *Bell Journal of Economics*, 13(2), 324–340. — the budget-balancing impossibility (§2).

Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature*, 596(7873), 583–589. — a research bottleneck absorbed into a tool (§5).

Korinek, A., and Stiglitz, J. E. (2019). Artificial intelligence and its implications for income distribution and unemployment. In A. Agrawal, J. Gans, and A. Goldfarb (Eds.), *The Economics of Artificial Intelligence: An Agenda* (pp. 349–390). University of Chicago Press. — shares not absolutes; immiseration amid growth (§6).

Kuznets, S. (1934). *National Income, 1929–1932*. National Bureau of Economic Research. — the architect's warning against reading welfare off national income (§8).

Lundberg, S. M., and Lee, S.-I. (2017). A unified approach to interpreting model predictions. In *Advances in Neural Information Processing Systems 30*. — SHAP; Shapley industrialized (§3).

Marx, K. (1867). *Capital: A Critique of Political Economy, Volume I*. Otto Meissner. (B. Fowkes, Trans., Penguin, 1976.) — surplus value as a class relation, not a metering (§2).

Maslej, N., Fattorini, L., Perrault, R., Gil, Y., Parli, V., et al. (2025). *The AI Index 2025 Annual Report*. AI Index Steering Committee, Stanford Institute for Human-Centered Artificial Intelligence. — macro motivation, prose only, no decimal claim (§5).

Milgrom, P., and Roberts, J. (1990). The economics of modern manufacturing: Technology, strategy, and organization. *American Economic Review*, 80(3), 511–528. — supermodular production; complementarity as the norm (§2).

Minsky, M. (1961). Steps toward artificial intelligence. *Proceedings of the IRE*, 49(1), 8–30. — credit assignment named at AI's founding (§1).

Neumann, J. von, and Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press. — the characteristic function (§2, §3). Bib form "Neumann ... von" so the surname token parses for `papers refs`; prose cites "von Neumann and Morgenstern".

Nordhaus, W. D. (2021). Are we approaching an economic singularity? Information technology and the future of economic growth. *American Economic Journal: Macroeconomics*, 13(1), 299–332. — singularity tests return "not yet" (§6, §9).

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press. — the do-operator; v(S) is interventional (§3).

Platz, J. von (2021). The principle of merit and the capital-labour split. *Economics and Philosophy*. — the meritocratic dilemma (§2). Bib form "Platz ... von" so the surname token parses for `papers refs`; prose cites "von Platz".

Polanyi, M. (1966). *The Tacit Dimension*. Doubleday. — we know more than we can tell; the verifier's residue (§7).

Reiff, M. R. (2013). *Exploitation and Economic Justice in the Liberal Capitalist State*. Oxford University Press. — Shapley as repair, rejected on desert grounds; the lead objection (§2, §9).

Ricardo, D. (1817). *On the Principles of Political Economy and Taxation*. John Murray. — distribution as the principal problem (§2).

Roemer, J. E. (1982). *A General Theory of Exploitation and Class*. Harvard University Press. — exploitation on coalitional counterfactuals (§2).

Shapley, L. S. (1953). A value for n-person games. In H. W. Kuhn and A. W. Tucker (Eds.), *Contributions to the Theory of Games, Volume II* (pp. 307–317). Princeton University Press. — the value; the paper's spine (§3 and throughout).

Shapley, L. S., and Shubik, M. (1954). A method for evaluating the distribution of power in a committee system. *American Political Science Review*, 48(3), 787–792. — the value as a power index (§2).

Shubik, M. (1962). Incentives, decentralized control, the assignment of joint costs and internal pricing. *Management Science*, 8(3), 325–343. — joint-cost allocation; the value as plumbing (§2).

Smith, A. (1776). *An Inquiry into the Nature and Causes of the Wealth of Nations*. W. Strahan and T. Cadell. — the pin factory; synergy without an instrument (§2).

Strathern, M. (1997). 'Improving ratings': Audit in the British university system. *European Review*, 5(3), 305–321. — the audit-culture form of Goodhart's law (§8).

Sutton, R. S., and Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. — RL as credit distribution among many decisions (§1).

Wicksteed, P. H. (1894). *An Essay on the Co-ordination of the Laws of Distribution*. Macmillan. — product exhaustion only under constant returns; the adding-up problem (§2).

Wolpert, D. H., and Tumer, K. (2001). Optimal payoff functions for members of collectives. *Advances in Complex Systems*, 4(2–3), 265–279. — difference rewards; the Shapley integrand from engineering (§3).

Wood, E. M. (1989). Rational choice Marxism: Is the game worth the candle? *New Left Review*, I/177, 41–88. — the internal rejection of game-theoretic Marxism (§2).

Young, H. P. (1988). Individual contribution and just compensation. In A. E. Roth (Ed.), *The Shapley Value: Essays in Honor of Lloyd S. Shapley*. Cambridge University Press. — the marginality axiomatization; prices the alternatives to averaging (§3, §9).
