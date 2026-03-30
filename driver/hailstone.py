"""Hailstone path driver.
Versions: many, prime, primeTop, rainbow, single
"""

import sys
import os
import math
import argparse

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from utils import is_prime, get_cmap, setup_output, save_figure

import matplotlib.pyplot as plt


output_dir = setup_output()

parser = argparse.ArgumentParser(description="Hailstone Driver")
parser.add_argument(
    "-v",
    "--version",
    required=True,
    choices=["many", "prime", "primeTop", "rainbow", "single"],
)
parser.add_argument("-p", "--plot", default=None)
parser.add_argument("-l", "--log", default=0, type=int)
parser.add_argument("-ht", "--height", default=0, type=int)
args = parser.parse_args()

version = args.version

# Set defaults based on version
if args.plot is None:
    args.plot = "27" if version == "single" else "list(range(1, 27))"

plotdata = eval(args.plot)
isLog = args.log
height = args.height


if version == "single":
    # === SINGLE VERSION ===
    n = plotdata

    plt.figure(figsize=(10, 5))
    plt.xlabel("Number of iterations")
    plt.ylabel("Number value")
    plt.title("Hailstone numbers: number %i" % n)

    # conut starts at 0 because the seed is not an iteration
    count = 0
    Arr = [[0], [n]]

    # for border of x axis
    if isLog == 2:
        count = 1
        Arr = [[1], [n]]

    print("Begin sequence: ")

    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
        count += 1
        Arr[0].insert(count, count)
        Arr[1].insert(count, n)

    print(n)

    x = Arr[0]
    y = Arr[1]

    # only for isLog == 3
    log_arr = np.log(Arr[1])

    if isLog == 3:
        # Perform linear regression
        X = np.arange(len(log_arr))
        slope, _ = np.polyfit(X, log_arr, 1)

        # Get the slope of the linear regression
        print("Linear Regression Slope: %f" % slope)

        # Create a new dataset by subtracting the slope of the linear regression
        noLog_dataset = log_arr - slope * X

    if isLog == 3:
        plt.plot(x, noLog_dataset, "k,-", linewidth=0.9)
    else:
        plt.plot(x, y, "k,-", linewidth=0.9)

    cmap = get_cmap(len(x))

    for k in range(count + 1):
        if isLog == 2:
            plt.plot(x[k - 1], y[k - 1], color=cmap(k), marker=".", markersize=1.9)
        elif isLog == 3:
            plt.plot(x[k], noLog_dataset[k], color=cmap(k), marker=".", markersize=1.9)
        else:
            plt.plot(x[k], y[k], color=cmap(k), marker=".", markersize=1.9)

    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)

    if isLog == 3:
        log_min = min(noLog_dataset)
        log_max = max(noLog_dataset)

    if isLog == 1:
        plt.yscale("log")
        plt.xlim(left=-0.0053 * max(x))
        plt.xlim(right=1.01 * max(x))
        plt.ylim(bottom=1 - 0.0075 * max(y))
        # log margins
        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    elif isLog == 2:
        plt.yscale("log")
        plt.xscale("log")
        # more log margins
        x_margin_log = (math.log10(x_max) - math.log10(x_min)) * 0.02
        plt.xlim(left=-0.0053 * max(x))
        plt.xlim(right=10 ** (math.log10(x_max) + x_margin_log))

        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        plt.ylim(bottom=1 - 0.0075 * max(y))
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    elif isLog == 3:
        plt.xlim(left=-0.0053 * max(x))
        plt.xlim(right=1.01 * max(x))
        plt.ylim(bottom=0.98 * log_min - 1)
        plt.ylim(top=1.02 * log_max)
    else:
        plt.xlim(left=-0.0053 * max(x))
        plt.xlim(right=1.01 * max(x))
        if height != 0:
            plt.ylim(top=height)
            plt.ylim(bottom=1 - 0.0075 * height)
        else:
            plt.ylim(bottom=1 - 0.0075 * max(y))
            plt.ylim(top=1.02 * max(y))

    save_figure(os.path.join(output_dir, "graph-single.png"))

else:
    # === MULTI VERSIONS: many, prime, primeTop, rainbow ===
    plotlist = plotdata
    PLlength = len(plotlist)

    plt.figure(figsize=(10, 5))
    plt.xlabel("Number of iterations")
    plt.ylabel("Number value")
    plt.title("Hailstone numbers comparison")

    maxlist = [[], []]

    def plot(n, color):
        count = 0
        Arr = [[0], [n]]
        if isLog == 2:
            count = 1
            Arr = [[1], [n]]
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = (n * 3) + 1
            count += 1
            Arr[0].insert(count, count)
            Arr[1].insert(count, n)
        x = Arr[0]
        y = Arr[1]
        plt.plot(x, y, ",-", linewidth=0.9, color=color)
        maxlist[0].append(max(x))
        maxlist[1].append(max(y))

    # Plot with version-specific coloring
    if version == "rainbow":
        cmap = get_cmap(PLlength + 1)
        for k in range(PLlength):
            plot(plotlist[k], cmap(k + 1))
    elif version == "primeTop":
        tmp = []
        for k in range(PLlength):
            if is_prime(plotlist[k]):
                tmp.append(plotlist[k])
            else:
                plot(plotlist[k], "blue")
        for j in range(len(tmp)):
            plot(tmp[j], "red")
    elif version == "prime":
        for k in range(PLlength):
            if is_prime(plotlist[k]):
                plot(plotlist[k], "red")
            else:
                plot(plotlist[k], "blue")
    else:  # many
        for k in range(PLlength):
            plot(plotlist[k], "blue")

    # Set axis limits
    x_min = min(maxlist[0])
    print("isLog: " + str(isLog) + ", x_min: " + str(x_min))
    x_max = max(maxlist[0])
    y_min = min(maxlist[1])
    y_max = max(maxlist[1])

    if isLog == 1:
        plt.yscale("log")
        plt.xlim(left=-0.0053 * max(maxlist[0]))
        plt.xlim(right=1.01 * max(maxlist[0]))
        plt.ylim(bottom=1 - 0.0075 * max(maxlist[1]))
        # log margins bruh
        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        if y_min == y_max:
            y_margin_log = 0.03
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    elif isLog == 2:
        plt.xscale("log")
        plt.yscale("log")
        # more log margins
        x_margin_log = (math.log10(x_max) - math.log10(x_min)) * 0.05
        if x_min == x_max:
            x_margin_log = 0.05
        plt.xlim(left=-0.0053 * max(maxlist[0]))
        plt.xlim(right=10 ** (math.log10(x_max) + x_margin_log))
        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        if y_min == y_max:
            y_margin_log = 0.03
        plt.ylim(bottom=1 - 0.0075 * max(maxlist[1]))
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    else:
        plt.xlim(left=-0.0053 * max(maxlist[0]))
        plt.xlim(right=1.01 * max(maxlist[0]))
        if height != 0:
            plt.ylim(top=height)
            plt.ylim(bottom=1 - 0.0075 * height)
        else:
            plt.ylim(bottom=1 - 0.0075 * max(maxlist[1]))
            plt.ylim(top=1.02 * max(maxlist[1]))

    save_figure(os.path.join(output_dir, "graph.png"))
