"""Sequence length driver.
Versions: reg, prime, primeTop, rainbow
"""

import sys
import os
import math
import argparse

sys.path.insert(0, os.path.dirname(__file__))
from utils import is_prime, get_cmap, setup_output, save_figure

import matplotlib.pyplot as plt


output_dir = setup_output()

parser = argparse.ArgumentParser(description="Sequence Length Driver")
parser.add_argument(
    "-v", "--version", required=True, choices=["reg", "prime", "primeTop", "rainbow"]
)
parser.add_argument("-p", "--plot", default="list(range(1, 101))")
parser.add_argument("-l", "--log", default=0, type=int)
parser.add_argument("-ht", "--height", default=0, type=int)
args = parser.parse_args()

version = args.version
plotlist = eval(args.plot)
isLog = args.log
height = args.height
PLlength = len(plotlist)

plt.figure(figsize=(10, 5))
plt.xlabel("Seed number")
plt.ylabel("Number of iterations")
plt.title("Hailstone path length")

maxlist = []


def PlotSeed(n, color):
    # count starts at 1 because the seed is part of the sequence
    count = 1
    originalN = n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
        count += 1

    maxlist.append(count)
    plt.plot(originalN, count, ".", color=color)


# Plot with version-specific coloring
if version == "rainbow":
    cmap = get_cmap(PLlength + 1)
    for k in range(PLlength):
        PlotSeed(plotlist[k], cmap(k + 1))
elif version == "primeTop":
    tmp = []
    for k in range(PLlength):
        if is_prime(plotlist[k]):
            tmp.append(plotlist[k])
        else:
            PlotSeed(plotlist[k], "blue")
    for j in range(len(tmp)):
        PlotSeed(tmp[j], "red")
elif version == "prime":
    for k in range(PLlength):
        if is_prime(plotlist[k]):
            PlotSeed(plotlist[k], "red")
        else:
            PlotSeed(plotlist[k], "blue")
else:  # reg
    for k in range(PLlength):
        PlotSeed(plotlist[k], "blue")

# Set axis limits
# margins with this is more complicated
# we calculate the margins as a percentage of the total range
x_min = min(plotlist)
x_max = max(plotlist)
y_min = min(maxlist)
y_max = max(maxlist)

x_margin = 0.02 * (x_max - x_min)
y_margin = 0.03 * (y_max - y_min)

if isLog == 1:
    plt.yscale("log")
    plt.xlim(left=x_min - x_margin)
    plt.xlim(right=x_max + x_margin)
    plt.ylim(bottom=y_min - y_margin)
    # log margins bruh
    y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
    if y_min == y_max:
        y_margin_log = 0.03
    plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
elif isLog == 2:
    plt.xscale("log")
    plt.yscale("log")
    # more log margins
    x_margin_log = (math.log10(x_max) - math.log10(x_min)) * 0.02
    plt.xlim(left=x_min - x_margin)
    plt.xlim(right=10 ** (math.log10(x_max) + x_margin_log))

    y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
    if y_min == y_max:
        y_margin_log = 0.03
    plt.ylim(bottom=y_min - y_margin)
    plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
else:
    plt.xlim(left=x_min - x_margin)
    plt.xlim(right=x_max + x_margin)
    if height != 0:
        plt.ylim(top=height)
        y_margin = 0.03 * (height - y_min)
        plt.ylim(bottom=y_min - y_margin)
    else:
        plt.ylim(bottom=y_min - y_margin)
        plt.ylim(top=y_max + y_margin)

save_figure(os.path.join(output_dir, "seedLen.png"))
