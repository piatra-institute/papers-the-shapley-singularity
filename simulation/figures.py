"""Publication figures for *The Shapley Singularity*. Pure plotters: every
value is read from the results dict produced by analyses.run(). Deterministic."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#1a1a1a"
ACCENT = "#b3202c"   # red
COOL = "#2a5b8c"     # blue
MUTE = "#8a8a8a"
PALE = "#b5b5b5"
GOLD = "#c98a1a"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.linewidth": 0.8,
})


# ---------------------------------------------------------------------------
def plot_attribution(results: dict, path: str) -> None:
    att = results["attribution"]
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.0))

    # --- left: the twenty units, naive vs Shapley ----------------------------
    gs = att["growth_shares"]
    rows = [("naive\n(growth / heads)", [("the ten hires", 20.0, ACCENT)]),
            ("Shapley", [("incumbent organization", gs["incumbents"], COOL),
                         ("the ten hires", gs["hires"], ACCENT),
                         ("demand wave", gs["demand"], MUTE)])]
    for y, (label, segs) in enumerate(reversed(rows)):
        left = 0.0
        for name, w, c in segs:
            axL.barh(y, w, left=left, height=0.52, color=c, alpha=0.92)
            if w >= 3.5:
                axL.text(left + w / 2, y, f"{name}\n{round(w, 2):g}", ha="center",
                         va="center", fontsize=8.2, color="white")
            else:
                axL.text(left + w / 2, y - 0.45, f"{name}: {round(w, 2):g}",
                         ha="center", va="top", fontsize=8.2, color=c)
            left += w
    axL.set_yticks([0, 1])
    axL.set_yticklabels([rows[1][0], rows[0][0]])
    axL.set_xlim(0, 20.6)
    axL.set_ylim(-0.55, 1.6)
    axL.set_xlabel("attributed share of the year's growth  (units of value)")
    axL.set_title("Who made the twenty units?", fontsize=10.5)

    # --- right: the Harsanyi ledger of the same twenty -----------------------
    d = att["harsanyi_dividends"]
    steps = [("incumbents x hires\n(splits 3 + 3)", d["incumbents_x_hires"], COOL),
             ("incumbents x demand\n(splits 5 + 5)", d["incumbents_x_demand"], MUTE),
             ("three-way synergy\n(splits 3 ways)", d["three_way"], GOLD)]
    bottom = 0.0
    for x, (label, h, c) in enumerate(steps):
        axR.bar(x, h, bottom=bottom, width=0.55, color=c, alpha=0.92)
        axR.text(x, bottom + h + 0.35, f"+{h:g}", ha="center", fontsize=9, color=c)
        bottom += h
    axR.axhline(20, color=INK, lw=0.9, ls="--")
    axR.text(-0.35, 20.45, "growth = 20", fontsize=8.5, ha="left")
    axR.annotate("exists only because all three\ncoincided; belongs to no one",
                 xy=(1.72, 17.6), xytext=(-0.35, 12.6), fontsize=8.2, color=GOLD,
                 arrowprops=dict(arrowstyle="->", color=GOLD, lw=1.1))
    axR.set_xticks(range(3))
    axR.set_xticklabels([s[0] for s in steps], fontsize=8.2)
    axR.set_ylim(0, 22.5)
    axR.set_ylabel("cumulative growth accounted for  (units)")
    axR.set_title("The same twenty as a ledger of interactions", fontsize=10.5)

    fig.suptitle("The attribution game: an exact three-player firm", fontsize=12, y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
def plot_compression(results: dict, path: str) -> None:
    comp = results["compression"]
    ver = results["verifier"]
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(13.6, 4.1))
    g = comp["grid"]

    # --- A: shares along the path at alpha = 6 -------------------------------
    axA.plot(g, comp["share_H"], color=INK, lw=1.8, label="human labor")
    axA.plot(g, comp["share_factor"], color=ACCENT, lw=1.8,
             label="intelligence = compute = energy")
    gx = comp["crossover_g_main"]
    i = g.index(gx)
    axA.scatter([gx], [comp["share_H"][i]], s=42, color=GOLD, zorder=5,
                edgecolor="white", linewidth=0.8)
    axA.annotate(f"crossover at g* = {gx:g}\n(g* = 3/alpha)".replace("alpha", r"$\alpha$"),
                 xy=(gx, comp["share_H"][i]), xytext=(0.56, 0.52),
                 fontsize=8.5, color=GOLD,
                 arrowprops=dict(arrowstyle="->", color=GOLD, lw=1.1))
    axA.text(1.0, comp["share_H"][-1] - 0.045, f'{comp["share_H"][-1]:g}',
             fontsize=8.5, color=INK, ha="right")
    axA.text(1.0, comp["share_factor"][-1] + 0.025, f'{comp["share_factor"][-1]:g}',
             fontsize=8.5, color=ACCENT, ha="right")
    axA.set_xlabel("automatable share of the task space  g")
    axA.set_ylabel("Shapley share of total value")
    axA.set_xlim(0, 1)
    axA.set_ylim(0, 1.04)
    axA.legend(frameon=False, fontsize=8.5, loc="upper right")
    axA.set_title(r"Shares along the path  ($\alpha = 6$)", fontsize=10.5)

    # --- B: the ceiling across the alpha family ------------------------------
    shades = {"3": PALE, "6": ACCENT, "12": MUTE, "48": INK}
    for a in map(str, comp["alphas"]):
        axB.plot(g, comp["psi_curves"][a], color=shades[a], lw=1.6)
        axB.text(1.005, comp["psi_curves"][a][-1], rf"$\alpha = {a}$",
                 fontsize=8.2, color=shades[a], va="center")
    cap = comp["ceiling_two_complements"]
    axB.axhline(cap, color=GOLD, lw=1.2, ls="--")
    axB.text(0.02, cap + 0.007, "ceiling 1/3: two essential complements,\n"
             "no finite productivity crosses it", fontsize=8.4, color=GOLD,
             va="bottom")
    axB.set_xlabel("automatable share of the task space  g")
    axB.set_ylabel("intelligence's share of total value")
    axB.set_xlim(0, 1.13)
    axB.set_ylim(0, 0.4)
    axB.set_title("The ceiling no capability crosses", fontsize=10.5)

    # --- C: the verification cliff at g = 1 ----------------------------------
    regimes = [("human\nverification", ver["human_verification"]),
               ("self-\nverification", ver["self_verification"])]
    labels = [("human labor (verifier)", "share_H", COOL),
              ("intelligence", "share_I", ACCENT),
              ("compute", "share_I", MUTE), ("energy", "share_I", PALE)]
    for y, (name, reg) in enumerate(reversed(regimes)):
        left = 0.0
        for lab, key, c in labels:
            w = reg["share_H"] if key == "share_H" else reg["share_I"]
            axC.barh(y, w, left=left, height=0.5, color=c, alpha=0.92)
            txt = f"{w:g}"
            axC.text(left + w / 2, y, txt, ha="center", va="center",
                     fontsize=8.2, color="white")
            left += w
    axC.annotate("the verifier's wage:\nlabor's share falls threefold",
                 xy=(0.0625, 0.28), xytext=(0.33, 0.44), fontsize=8.4, color=COOL,
                 arrowprops=dict(arrowstyle="->", color=COOL, lw=1.1))
    axC.set_yticks([0, 1])
    axC.set_yticklabels([r[0] for r in reversed(regimes)], fontsize=8.6)
    axC.set_xlim(0, 1)
    axC.set_ylim(-0.6, 1.75)
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for _, _, c in labels]
    axC.legend(handles, [l[0] for l in labels], frameon=False, fontsize=7.8,
               loc="upper center", ncol=2)
    axC.set_xlabel("share of total value at g = 1")
    axC.set_title("The verification cliff", fontsize=10.5)

    fig.suptitle("The compression path: the rise of intelligence's share, and its ceilings",
                 fontsize=12, y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
