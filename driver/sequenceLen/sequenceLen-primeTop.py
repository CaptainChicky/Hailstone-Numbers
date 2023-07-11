import math
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))

import os
import argparse

# Create a directory for saving figures if it doesn't exist
output_directory = 'generated'
os.makedirs(output_directory, exist_ok=True)

plt.xlabel('Seed number')
plt.ylabel('Number of iterations')
plt.title('Hailstone path length')

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    

maxlist = []

plotlist = []

isLog = 0

# Create the argument parser
parser = argparse.ArgumentParser(description='Driver Program')

# Add an optional option for the plot argument
parser.add_argument('-p', '--plot', help='List of values for plotting', default='list(range(1, 101))')
parser.add_argument('-l', '--log', help='Log axis scaling, 0 for non, 1 for y axis, 2 for both', default=0, type=int)

# Parse the command-line arguments
args = parser.parse_args()

# Parse the plot argument into a list
plotlist = eval(args.plot)
isLog = args.log


PLlength = len(plotlist)

def PlotSeed(n, color):
    # count starts at 1 because the seed is part of the sequence
    count = 1
    originalN = n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = ((n * 3) + 1)
        count += 1

    maxlist.append(count)
    plt.plot(originalN, count, '.', color=color)

def plotall():
    color = "blue"
    tmp = []
    for k in range(PLlength):
        if isPrime(plotlist[k]):
            tmp.append(plotlist[k])
        else:
            PlotSeed(plotlist[k], color)
    
    for j in range(len(tmp)):
        PlotSeed(tmp[j], "red")

    # margins with this is more complicated
    # we calculate the margins as a percentage of the total range
    x_min = min(plotlist)
    x_max = max(plotlist)
    y_min = min(maxlist)
    y_max = max(maxlist)

    x_margin = 0.02 * (x_max - x_min)
    y_margin = 0.03 * (y_max - y_min)

    if isLog == 1:
        plt.yscale('log')
        plt.xlim(left=x_min - x_margin)
        plt.xlim(right=x_max + x_margin)
        plt.ylim(bottom=y_min - y_margin)
        # log margins bruh
        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        if y_min == y_max:
            y_margin_log = 0.03
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    elif isLog == 2:
        plt.xscale('log')
        plt.yscale('log')
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
        plt.ylim(bottom=y_min - y_margin)
        plt.ylim(top=y_max + y_margin)

plotall()

txt = "Made by Chicky"
#first num is percent on x axis, second is y
plt.figtext(0.075, 0.065, txt, wrap=True, horizontalalignment='center', fontsize=8, color="grey")

plt.tight_layout()

dpi = 500
plt.subplots_adjust(left=0.15, bottom=0.1)

# Save the figure in the specified directory
filename = os.path.join(output_directory, 'seedLen.png')
plt.savefig(filename, dpi=dpi)