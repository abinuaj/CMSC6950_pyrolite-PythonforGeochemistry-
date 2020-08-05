import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyrolite.plot import pyroplot


data = pd.read_csv('https://drive.google.com/uc?export=download&id=1bK070E8K8ysok_wxAV582Yy-i9bbJA2s')
df=pd.DataFrame(data)

from pyrolite.comp.codata import logratiomean
import itertools

fig, ax = plt.subplots(2, 2, figsize=(16, 12), subplot_kw=dict(projection="ternary"))
ax = ax.flat

for columns, a in zip(itertools.combinations(["Food_waste", "Paper", "Wood", "Textiles","Noncombustibles","Glass","Metal"], 3), ax):
    columns = list(columns)

    df.loc[:, columns].pyroplot.scatter(
        ax=a, color="b", marker=".",label="muncipality waste" ,no_ticks=True
    )

    df.mean().loc[columns].pyroplot.scatter(
        ax=a,
        edgecolors="red",
        linewidths=2,
        c="none",
        s=50,
        label="Arithmetic Mean",
        no_ticks=True,
    )

    logratiomean(df.loc[:, columns]).pyroplot.scatter(
        ax=a,
        edgecolors="k",
        linewidths=2,
        c="none",
        s=50,
        label="Geometric Mean",
        axlabels=True,
        no_ticks=True,
    )
    a.legend(frameon=False, facecolor=None, loc=(0.8, 0.5))
plt.savefig('ternary.png')


# Second Plot

from scipy.stats import norm, poisson, lognorm

means = [[10, 10], [10, 20], [20, 100], [1000, 50]]
fig, ax = plt.subplots(len(means), 4, figsize=(12, 8))
ax[0, 0].set_title("Food_waste")
ax[0, 1].set_title("Plastics")
ax[0, 2].set_title("Normal Fit to Plastics/Food_waste")
ax[0, 3].set_title("Lognormal Fit to Plastics/Food_waste")
ax[-1, 0].set_xlabel("Food_waste")
ax[-1, 1].set_xlabel("Plastics")
ax[-1, 2].set_xlabel("Plastics/Food_waste")
ax[-1, 3].set_xlabel("Plastics/Food_waste")
for ix, (m1, m2) in enumerate(means):
    p1, p2 = poisson(mu=m1), poisson(mu=m2)
    y1, y2 = p1.rvs(2000), p2.rvs(2000)
    ratios = y2[y1 > 0] / y1[y1 > 0]

    y1min, y1max = y1.min(), y1.max()
    y2min, y2max = y2.min(), y2.max()
    ax[ix, 0].hist(
        y1,
        color="0.5",
        alpha=0.6,
        label="Food_waste",
        bins=np.linspace(y1min - 0.5, y1max + 0.5, (y1max - y1min) + 1),
    )
    ax[ix, 1].hist(
        y2,
        color="0.5",
        alpha=0.6,
        label="Plastics",
        bins=np.linspace(y2min - 0.5, y2max + 0.5, (y2max - y2min) + 1),
    )

    # normal distribution fit
    H, binedges, patches = ax[ix, 2].hist(
        ratios, color="Purple", alpha=0.6, label="Ratios", bins=100
    )
    loc, scale = norm.fit(ratios, loc=0)
    pdf = norm.pdf(binedges, loc, scale)
    twin2 = ax[ix, 2].twinx()
    twin2.set_ylim(0, 1.1 * np.max(pdf))
    twin2.plot(binedges, pdf, color="k", ls="--", label="Normal Fit")

    # log-normal distribution fit
    H, binedges, patches = ax[ix, 3].hist(
        ratios, color="Green", alpha=0.6, label="Ratios", bins=100
    )
    s, loc, scale = lognorm.fit(ratios, loc=0)
    pdf = lognorm.pdf(binedges, s, loc, scale)
    twin3 = ax[ix, 3].twinx()
    twin3.set_ylim(0, 1.1 * np.max(pdf))
    twin3.plot(binedges, pdf, color="k", ls="--", label="Lognormal Fit")

    for a in [*ax[ix, :], twin2, twin3]:
        a.set_yticks([])

plt.tight_layout()
plt.savefig('lognormal.png')
