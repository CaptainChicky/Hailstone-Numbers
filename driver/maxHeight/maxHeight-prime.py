import math
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import os
import argparse

# Create a directory for saving figures if it doesn't exist
output_directory = 'generated'
os.makedirs(output_directory, exist_ok=True)


# fix and definetely use log plot later lmao
plt.figure(figsize=(8, 12.5))
plt.xlabel('Seed value')
plt.ylabel('Maximum value')
plt.title('Hailstone maximums')

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
height = 0

# Create the argument parser
parser = argparse.ArgumentParser(description='Driver Program')

# Add an optional option for arguments
parser.add_argument('-p', '--plot', help='List of values for plotting', default='list(range(1, 101))')
parser.add_argument('-l', '--log', help='Log axis scaling, 0 for non, 1 for y axis, 2 for both', default=1, type=int)
parser.add_argument('-ht', '--height', help='Specify the height of a graph', default=0, type=int)

# Parse the command-line arguments
args = parser.parse_args()

# Parse the plot argument into a list
plotlist = eval(args.plot)
isLog = args.log
height = args.height

PLlength = len(plotlist)

def plot(n, color):
    Arr = [n]
    originalN = n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = ((n * 3) + 1)
        Arr.append(n)

    x = originalN
    y = max(Arr)
    
    maxlist.append(y)

    plt.plot(x, y, '.', color=color)

def plotall():
    color = "blue"
    for k in range(PLlength):
        if isPrime(plotlist[k]):
            plot(plotlist[k], 'red')
        else:
            plot(plotlist[k], color)


    # margins with this is more complicated
    # we calculate the margins as a percentage of the total range
    x_min = min(plotlist)
    x_max = max(plotlist)
    y_min = min(maxlist)
    y_max = max(maxlist)

    x_margin = 0.02 * (x_max - x_min)
    y_margin_top = 0.03 * (y_max - y_min)
    y_margin_bottom = 0.01 * (y_max - y_min)

    if isLog == 1:
        plt.yscale('log')
        plt.xlim(left=x_min - x_margin)
        plt.xlim(right=x_max + x_margin)
        plt.ylim(bottom=y_min - y_margin_bottom)
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
        plt.ylim(bottom=y_min - y_margin_top)
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    else:
        plt.xlim(left=x_min - x_margin)
        plt.xlim(right=x_max + x_margin)
        if height != 0:
            plt.ylim(top=height)
            y_margin_bottom = 0.01 * (height - y_min)
            plt.ylim(bottom=y_min - y_margin_bottom)
        else:
            plt.ylim(top=y_max + y_margin_top * 0.5)
            plt.ylim(bottom=y_min - y_margin_bottom)

plotall()


txt = "Made by Chicky"

x_percent = 0.04
y_percent = 0.015

# Add the text with fixed pixel values
plt.figtext(x_percent, y_percent, txt, wrap=True, horizontalalignment='left', fontsize=8, color="grey")


plt.tight_layout()
 
plt.subplots_adjust(left=0.15, bottom=0.05)

filename = os.path.join(output_directory, 'maxgraph.pdf')
plt.savefig(filename, format='pdf')
