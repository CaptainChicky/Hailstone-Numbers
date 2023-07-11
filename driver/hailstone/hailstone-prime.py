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


plt.xlabel('Number of iterations')
plt.ylabel('Number value')
plt.title('Hailstone numbers comparison')

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

maxlist = [[], []]

plotlist = []

isLog = 0
height = 0

# Create the argument parser
parser = argparse.ArgumentParser(description='Driver Program')

# Add an optional option for the plot argument
parser.add_argument('-p', '--plot', help='List of values for plotting', default='list(range(1, 27))')
parser.add_argument('-l', '--log', help='Log axis scaling, 0 for non, 1 for y axis, 2 for both', default=0, type=int)
parser.add_argument('-ht', '--height', help='Specify the height of a graph', default=0, type=int)

# Parse the command-line arguments
args = parser.parse_args()

# Parse the plot argument into a list
plotlist = eval(args.plot)
isLog = args.log
height = args.height


PLlength = len(plotlist)

def plot(n, color):
    # count starts at 0 because the beginning number is not an iteration
    count = 0
    Arr = [[0], [n]]

    # for border of x axis
    if isLog == 2:
        count = 1
        Arr = [[1], [n]]

    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = ((n * 3) + 1)
        count += 1

        Arr[0].insert(count, count)
        Arr[1].insert(count, n)

    x = Arr[0]
    y = Arr[1]

    plt.plot(x, y, ',-', linewidth=0.9, color=color)

    maxlist[0].append(max(x))
    maxlist[1].append(max(y))

def plotall():
    color = "blue"
    for k in range(PLlength):
        if isPrime(plotlist[k]):
            plot(plotlist[k], 'red')
        else:
            plot(plotlist[k], color)


    x_min = min(maxlist[0])
    print("isLog: " + str(isLog) + ", x_min: " + str(x_min))
    x_max = max(maxlist[0])
    y_min = min(maxlist[1])
    y_max = max(maxlist[1])

    if isLog == 1:
        plt.yscale('log')
        plt.xlim(left=-0.0053 * max(maxlist[0]))
        plt.xlim(right=1.01 * max(maxlist[0]))
        plt.ylim(bottom=1-0.0075 * max(maxlist[1]))
        # log margins bruh
        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        if y_min == y_max:
            y_margin_log = 0.03
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    elif isLog == 2:
        plt.xscale('log')
        plt.yscale('log')
        # more log margins
        x_margin_log = (math.log10(x_max) - math.log10(x_min)) * 0.05
        if x_min == x_max:
            x_margin_log = 0.05
        plt.xlim(left=-0.0053 * max(maxlist[0]))
        plt.xlim(right=10 ** (math.log10(x_max) + x_margin_log))
        
        y_margin_log = (math.log10(y_max) - math.log10(y_min)) * 0.03
        if y_min == y_max:
            y_margin_log = 0.03
        plt.ylim(bottom=1-0.0075 * max(maxlist[1]))
        plt.ylim(top=10 ** (math.log10(y_max) + y_margin_log))
    else:
        plt.xlim(left=-0.0053 * max(maxlist[0]))
        plt.xlim(right=1.01 * max(maxlist[0]))
        if height != 0:
            plt.ylim(top=height)
            plt.ylim(bottom=1-0.0075 * height)
        else:
            plt.ylim(bottom=1-0.0075 * max(maxlist[1]))
            plt.ylim(top=1.02 * max(maxlist[1]))


plotall()

txt = "Made by Chicky"
#first num is percent on x axis, second is y
plt.figtext(0.075, 0.065, txt, wrap=True, horizontalalignment='center', fontsize=8, color="grey")

plt.tight_layout()

dpi = 500
plt.subplots_adjust(left=0.15, bottom=0.1)

# Save the figure in the specified directory
filename = os.path.join(output_directory, 'graph.png')
plt.savefig(filename, dpi=dpi)