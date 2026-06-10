"""Exact cooperative-game analyses for *The Shapley Singularity*.

Three deterministic analyses, no seed, no floating-point estimation: every
Shapley value is computed by full enumeration of orderings in exact rational
arithmetic (fractions.Fraction), every Harsanyi dividend by exact Mobius
inversion, and the closed forms quoted in the paper are asserted against the
enumeration before anything is written out.

  attribution_game   - the firm puzzle (incumbents, hires, demand) solved
                       exactly: naive growth-per-head vs Shapley vs the
                       Harsanyi synergy ledger; plus Cohen's land/labour game
                       and the symmetric complement pair.
  compression_path   - a task-continuum production game over {intelligence,
                       compute, energy, humans}: exact Shapley curves in the
                       automatable share g and the AI productivity multiple
                       alpha; the I=C=E symmetry, the crossover g* = 3/alpha,
                       and the 1/(k+1) ceiling on intelligence's share.
  verifier_and_power - the verification regimes at full automatability (human
                       verification vs self-verification: the verifier's wage
                       and the cliff), and the core of the limit games (the
                       bargaining zone around the Shapley point).
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations

F = Fraction


# ---------------------------------------------------------------------------
# exact machinery
# ---------------------------------------------------------------------------
def shapley(players: tuple, v) -> dict:
    """Exact Shapley values by full enumeration of all |N|! orderings."""
    phi = {p: F(0) for p in players}
    count = 0
    for order in permutations(players):
        seen: set = set()
        for p in order:
            before = frozenset(seen)
            seen.add(p)
            phi[p] += v(frozenset(seen)) - v(before)
        count += 1
    return {p: phi[p] / count for p in players}


def dividends(players: tuple, v) -> dict:
    """Exact Harsanyi dividends d(S) by Mobius inversion of v."""
    out = {}
    for r in range(1, len(players) + 1):
        for S in combinations(players, r):
            d = F(0)
            for rr in range(0, r + 1):
                for T in combinations(S, rr):
                    d += (-1) ** (r - rr) * v(frozenset(T))
            out[frozenset(S)] = d
    return out


def fl(x: Fraction, nd: int = 4) -> float:
    return round(float(x), nd)


# ---------------------------------------------------------------------------
# analysis 1 - the attribution game
# ---------------------------------------------------------------------------
def attribution_game() -> dict:
    """The firm puzzle: 100 units before, ten hires, 120 after. Who made 20?

    Three players: O, the incumbent organization (existing team, product,
    assets, as one bloc); N, the ten new hires as a bloc; M, the favorable
    market (the demand wave the firm rode that year). The coalition function
    records what each combination would have produced:

      v(O) = 100         the firm as it was
      v(O,M) = 110       the old firm riding the wave alone
      v(O,N) = 106       the enlarged firm in a flat market
      v(O,N,M) = 120     the observed year
      v of anything without O = 0   (hires and demand make nothing alone)
    """
    O, N, M = "incumbents", "hires", "demand"
    table = {
        frozenset(): F(0),
        frozenset({O}): F(100),
        frozenset({N}): F(0),
        frozenset({M}): F(0),
        frozenset({O, N}): F(106),
        frozenset({O, M}): F(110),
        frozenset({N, M}): F(0),
        frozenset({O, N, M}): F(120),
    }
    v = table.__getitem__
    players = (O, N, M)
    phi = shapley(players, v)
    div = dividends(players, v)

    # exact checks: efficiency, and the dividend ledger reassembles v(N)
    assert sum(phi.values()) == F(120)
    assert sum(div.values()) == F(120)
    assert phi[N] == F(26, 6) and phi[M] == F(38, 6) and phi[O] == F(656, 6)
    assert div[frozenset({O, N, M})] == F(4)

    growth = F(20)
    growth_shares = {O: phi[O] - F(100), N: phi[N], M: phi[M]}
    assert sum(growth_shares.values()) == growth

    per_hire = phi[N] / 10
    naive_per_hire = growth / 10

    # Cohen's land/labour game: land alone 1, labour alone 0, together 10
    L, W = "land", "labour"
    cohen_v = {
        frozenset(): F(0), frozenset({L}): F(1),
        frozenset({W}): F(0), frozenset({L, W}): F(10),
    }.__getitem__
    cohen = shapley((L, W), cohen_v)
    assert cohen[L] == F(11, 2) and cohen[W] == F(9, 2)

    # the symmetric complement pair: nothing alone, everything together
    eng, sal = "engineer", "salesperson"
    pair_v = {
        frozenset(): F(0), frozenset({eng}): F(0),
        frozenset({sal}): F(0), frozenset({eng, sal}): F(100),
    }.__getitem__
    pair = shapley((eng, sal), pair_v)
    assert pair[eng] == pair[sal] == F(50)

    return {
        "v": {"O": 100, "N_alone": 0, "M_alone": 0, "ON": 106, "OM": 110,
              "NM": 0, "ONM": 120},
        "shapley": {k: fl(x) for k, x in phi.items()},
        "growth_total": 20,
        "growth_shares": {k: fl(x) for k, x in growth_shares.items()},
        "per_hire_shapley": fl(per_hire),
        "per_hire_naive": fl(naive_per_hire),
        "naive_overstatement": fl(naive_per_hire / per_hire),
        "harsanyi_dividends": {
            "incumbents_alone": fl(div[frozenset({O})]),
            "hires_alone": fl(div[frozenset({N})]),
            "demand_alone": fl(div[frozenset({M})]),
            "incumbents_x_hires": fl(div[frozenset({O, N})]),
            "incumbents_x_demand": fl(div[frozenset({O, M})]),
            "hires_x_demand": fl(div[frozenset({N, M})]),
            "three_way": fl(div[frozenset({O, N, M})]),
        },
        "cohen_land_labour": {"land": fl(cohen[L]), "labour": fl(cohen[W])},
        "complement_pair": {"engineer": fl(pair[eng]), "salesperson": fl(pair[sal])},
    }


# ---------------------------------------------------------------------------
# analysis 2 - the compression path
# ---------------------------------------------------------------------------
# Factors: I intelligence, C compute, E energy, H human labor. A unit
# continuum of tasks; a share g is automatable. Humans do any task at
# productivity 1. The full stack {I,C,E} does automatable tasks at
# productivity alpha. Each task is performed by the best producer present:
#
#   v_g(S) = (1-g) * [H in S]  +  g * max( alpha * [{I,C,E} <= S], [H in S] )
#
# Closed forms (asserted below against full enumeration):
#   phi_H(g) = 1 - g/4            phi_I = phi_C = phi_E = g(4*alpha-3)/12
#   v(N)     = 1 + (alpha-1) g    crossover phi_I = phi_H at g* = 3/alpha
#   share_I(g=1) = (4*alpha-3)/(12*alpha)  ->  1/3 as alpha -> inf
I, C, E, H = "I", "C", "E", "H"
STACK = frozenset({I, C, E})
FACTORS = (I, C, E, H)


def v_compression(g: Fraction, alpha: Fraction):
    def v(S: frozenset) -> Fraction:
        human = F(1) if H in S else F(0)
        ai = alpha if STACK <= S else F(0)
        return (1 - g) * human + g * max(ai, human)
    return v


def compression_path() -> dict:
    alpha_main = F(6)
    alphas = [F(3), F(6), F(12), F(48)]
    grid = [F(i, 40) for i in range(41)]

    # exact curves at alpha_main
    share_H, share_factor, phi_H_abs, phi_I_abs, total = [], [], [], [], []
    for g in grid:
        phi = shapley(FACTORS, v_compression(g, alpha_main))
        vN = 1 + (alpha_main - 1) * g
        assert phi[H] == 1 - g / 4
        assert phi[I] == phi[C] == phi[E] == g * (4 * alpha_main - 3) / 12
        assert sum(phi.values()) == vN
        share_H.append(fl(phi[H] / vN))
        share_factor.append(fl(phi[I] / vN))
        phi_H_abs.append(fl(phi[H]))
        phi_I_abs.append(fl(phi[I]))
        total.append(fl(vN))

    # intelligence-share curves and endpoints across the alpha family
    psi_curves, psi_at_1, crossover = {}, {}, {}
    for a in alphas:
        curve = []
        for g in grid:
            phi = shapley(FACTORS, v_compression(g, a))
            curve.append(fl(phi[I] / (1 + (a - 1) * g)))
        psi_curves[str(int(a))] = curve
        psi_at_1[str(int(a))] = fl((4 * a - 3) / (12 * a))
        gs = F(3) / a                      # phi_I(g*) = phi_H(g*), exactly
        phi_star = shapley(FACTORS, v_compression(gs, a))
        assert phi_star[I] == phi_star[H]
        crossover[str(int(a))] = fl(gs)

    # the ceiling: with k essential complements the limit game is the
    # unanimity game on {I} u B, so intelligence's share is exactly 1/(k+1)
    caps = {}
    for k in range(1, 6):
        players = ("I",) + tuple(f"B{j}" for j in range(1, k + 1))
        full = frozenset(players)
        u = lambda S, full=full: F(1) if S == full else F(0)
        phi = shapley(players, u)
        assert phi["I"] == F(1, k + 1)
        caps[f"k{k}"] = fl(F(1, k + 1))

    phi_end = shapley(FACTORS, v_compression(F(1), alpha_main))
    return {
        "alpha_main": int(alpha_main),
        "alphas": [int(a) for a in alphas],
        "grid": [fl(g) for g in grid],
        "share_H": share_H,
        "share_factor": share_factor,         # I = C = E for every g
        "phi_H_abs": phi_H_abs,
        "phi_I_abs": phi_I_abs,
        "total_value": total,
        "labor_share_start": 1.0,
        "labor_share_end": fl(phi_end[H] / 6),
        "phi_H_end_abs": fl(phi_end[H]),
        "psi_curves": psi_curves,
        "psi_at_1": psi_at_1,
        "crossover_g": crossover,
        "crossover_g_main": crossover[str(int(alpha_main))],
        "ceiling_two_complements": fl(F(1, 3)),
        "unanimity_caps": caps,
        "output_multiple_at_1": fl(1 + (alpha_main - 1)),
    }


# ---------------------------------------------------------------------------
# analysis 3 - the verifier's wage and the bargaining zone
# ---------------------------------------------------------------------------
def verifier_and_power() -> dict:
    """Two regimes at g = 1 (every task automatable), alpha = 6.

    Human verification: machine output counts only when a human verifies it,
    so the automated route needs the whole of {I,C,E,H}; humans alone still
    produce 1 by working manually.

        v(S) = alpha if {I,C,E,H} <= S;  1 if H in S;  0 otherwise.

    Self-verification: the system verifies its own output; the game is the
    g = 1 compression game, v(S) = max(alpha*[{I,C,E} <= S], [H in S]).

    Then the core: in the human-verification game labor's core floor is its
    outside option; in the displacement limit (humans gone, unanimity game on
    {I,C,E}) the core is the entire simplex while the Shapley point is 1/3.
    """
    alpha = F(6)

    def v_human(S: frozenset) -> Fraction:
        if STACK <= S and H in S:
            return alpha
        return F(1) if H in S else F(0)

    v_self = v_compression(F(1), alpha)

    ph = shapley(FACTORS, v_human)
    ps = shapley(FACTORS, v_self)
    assert ph[H] == F(9, 4) and ph[I] == ph[C] == ph[E] == F(5, 4)
    assert ps[H] == F(3, 4) and ps[I] == ps[C] == ps[E] == F(7, 4)

    vN = F(6)
    human = {"phi_H": fl(ph[H]), "phi_I": fl(ph[I]),
             "share_H": fl(ph[H] / vN), "share_I": fl(ph[I] / vN)}
    self_ = {"phi_H": fl(ps[H]), "phi_I": fl(ps[I]),
             "share_H": fl(ps[H] / vN), "share_I": fl(ps[I] / vN)}

    cliff_abs = ph[H] - ps[H]
    assert cliff_abs == F(3, 2)
    drop_factor = ph[H] / ps[H]
    assert drop_factor == F(3)

    # core of the human-verification game: x_H in [v({H}), v(N)] = [1, 6];
    # every coalition without H is worth 0, so no complement has a floor.
    core_human = {
        "labor_floor": 1.0, "labor_floor_share": fl(F(1, 6)),
        "labor_shapley_share": fl(ph[H] / vN),
        "labor_ceiling_share": 1.0,
    }
    # displacement limit: unanimity game on {I,C,E} worth alpha; the core is
    # every nonnegative split of alpha, the Shapley point is alpha/3 each.
    trio = (I, C, E)
    u = lambda S: alpha if S == frozenset(trio) else F(0)
    pu = shapley(trio, u)
    assert pu[I] == pu[C] == pu[E] == F(2)
    core_unanimity = {
        "shapley_point_share": fl(F(1, 3)),
        "core_min_share": 0.0,
        "core_max_share": 1.0,
        "shapley_point_abs": fl(pu[I]),
    }

    return {
        "alpha": int(alpha),
        "human_verification": human,
        "self_verification": self_,
        "cliff_abs": fl(cliff_abs),
        "cliff_share": fl(cliff_abs / vN),
        "labor_drop_factor": fl(drop_factor),
        "core_human_verification": core_human,
        "core_unanimity_limit": core_unanimity,
    }


# ---------------------------------------------------------------------------
def run() -> dict:
    return {
        "attribution": attribution_game(),
        "compression": compression_path(),
        "verifier": verifier_and_power(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
